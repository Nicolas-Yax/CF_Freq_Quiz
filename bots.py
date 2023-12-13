from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import multiprocessing as mp
# from multiprocessing.pool import ThreadPool
import threading
import argparse
import time
import os
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import queue
import matplotlib.pyplot as plt


# PUT YOUR OWN PATH HERE
# if os is windows
if os.name == 'nt':
    CHROMEDRIVER = \
        'C:/Users/Basile/.wdm/drivers/chromedriver/win32/90.0.4430.24/chromedriver.exe'
# if os is linux
else:
    CHROMEDRIVER = '/snap/bin/chromium.chromedriver'


class Bot:
    def __init__(self, idx, url, slow=False):
        super().__init__()

        self.idx = idx

        with mp.Lock():
            options = webdriver.ChromeOptions()
            #  uncomment to open windows in the background
            # options.add_argument('headless')
            self.driver = webdriver.Chrome(CHROMEDRIVER, options=options)
            self.driver.get(url)
            if slow:
                print(f'Bot {self.idx}: slow mode')
                self.driver.set_network_conditions(
                    offline=False,
                    latency=15000,  # additional latency (ms)
                    download_throughput=500 * 1024,  # maximal throughput
                    upload_throughput=500 * 1024)  # maximal throughput

    def find_endlessly(self, el_id):
        while True:
            try:
                return self.driver.find_element_by_id(el_id)

            except Exception as e:
                print(f'Bot {self.idx}: {e}')
                time.sleep(.2)

    def find(self, el_id):
        try:
            return self.driver.find_element_by_id(el_id)
        except Exception as e:
            print(f'Bot {self.idx}: {e}')
            return None

    def wait_until_el(self, el_id):
        timeout = 5
        try:
            element_present = EC.presence_of_element_located((By.ID, el_id))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print(f"Bot {self.idx}: Timed out waiting for page to load")
            time.sleep(.2)

    def get_value(self, el_id):
        return self.driver.find_element_by_id(el_id).get_attribute('value')

    # def get_phaseNum(self):
        # return self.driver.execute_script('return localStorage["phaseNum"]')

    def set_value(self, el_id, v):
        self.driver.execute_script(f"$('#{el_id}').val({v})")

    def find_and_click(self, el_id):
        el = self.find(el_id)
        if el is not None:
            try:
                el.click()
                return True
            except:
                pass
        return None


class SurveyAgent(Bot):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def run(self, q):
        while True:

            try:

                # ----------------------------------------------------------- #
                # fill inputs
                # ----------------------------------------------------------- #
                if self.find('fname0'):
                    self.find_and_click('fname0')
                    self.find('fname0').send_keys( ['Yes', 'No'][np.random.randint(2)])
                    self.find_and_click('fname1')
                    self.find('fname1').send_keys('Because it is what it is!!!')

                # ----------------------------------------------------------- #
                # continue
                # ----------------------------------------------------------- #
                if self.find_and_click('next'):
                    time.sleep(0.5)


                # in case you want to transmit live data to the main thread
                # q.put({'reset': False, 'data': [corr, t]})

                # if some element appears on the page, stop the thread/bot
                if self.find('end'):
                    # end thread
                    break

            except Exception as e:
                print(f'Error: {e}')
                time.sleep(1)
                continue

            time.sleep(3)


def run(idx, url, slow):

    b = SurveyAgent(
        url=url+f"?PROLIFIC_PID=Bob{idx}", idx=idx, slow=slow)

    print(f'Bot {b.idx} is running')
    b.run(q)


if __name__ == '__main__':
    # run in terminal like
    # python bots.py -u <your task url> -n <number of bots you desire> 
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='link for the experiment')
    parser.add_argument('-n', '--nbot', help='number of bots')
    parser.add_argument('-s', '--slow', help='slow bots (3g/2g connection)', action='store_true')
    args = parser.parse_args()

    n_bot = int(args.nbot)
    n_process = n_bot

    # queue use to transmit information between the main thread and the other threads (the bots)
    # q.put(args) is used to put something in the queue in a certain thread
    # q.get() is used to get the information from another thread
    q = queue.LifoQueue()

    np.random.seed(1)


    # run one thread per bot
    for i in range(n_bot):
        t = threading.Thread(target=run, args=(
            i, args.url, args.slow))
        t.start()

    # -----------------------------------------------------------------------------#
    # Plot some data in real time using queue
    # ---------------------------------------------------------------------------- # 
    # fig, ax = plt.subplots(
    #     1, 1, figsize=(10, 8))

    # d = {}

    # while True:
    #     out = q.get()
    #     if out['reset']:
    #         d = {}
    #     try:
    #         t = out['data'][0]
    #         out = out['data'][1]

    #         if t not in d:
    #             d[t] = []

    #         d[t].append(out)

    #         m = np.array([np.mean(d[i]) for i in range(max(d.keys()))])
    #         sem = np.array([stats.sem(d[i]) for i in range(max(d.keys()))])
    #         x = list(range(len(m)))

    #         ax.clear()

    #         ax.plot(x, m, color='C0')
    #         ax.fill_between(x=x, y1=m+sem, y2=m-sem, color='C0', alpha=.2)

    #         ax.set_ylim([0, 1])

    #         ax.set_xlabel('t')
    #         ax.set_ylabel('Correct choice rate')

    #         plt.draw()
    #         plt.pause(.1)
    #     except:
    #         pass
