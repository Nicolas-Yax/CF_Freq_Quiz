export const dataset = {
	name: "Cushman",
	instructions: [

		{
			title: "Consent",
			items: [
				{
					text: `You are about to participate in a psychological research study.
					This study aims to understand how people solve short questions.
					The proposed experiments have no immediate application or clinical value, but they will allow us to improve our understanding of moral reasoning in humans. We are asking you to participate in this study because you have been recruited on the Prolific platform.`,
					type: "regular",
					variables: [],
					title: "Information for the participant"
				},
				{
					text: `During your participation in this study, we will ask you to answer several simple questionnaires and tests, which do not require any particular competence.Your internet-based participation will require approximately 10 minutes or possibly less.`,
					type: "regular",
					variables: [],
					title: "Procedure"
				},
				{
					text: `Your participation in this study is voluntary. This means that you are consenting to participate in this project without external pressure.During your participation in this project, the researcher in charge and his staff will collect and record information about you. In order to preserve your identity and the confidentiality of the data, the identification of each file will be coded, thus preserving the anonymity of your answers. We will not collect any personal data from the RISC or Prolific platforms. The researcher in charge of this study will only use the data for research purposes in order to answer the scientific objectives of the project.The data may be published in scientific journals and shared within the scientific community, in which case no publication or scientific communication will contain identifying information.`,
					type: "regular",
					variables: [],
					title: "Voluntary Participation And Confidentiality"
				},
				{
					text: "I'm 18 years old or older",
					type: "checkbox",
				},
				{
					text: "My participation in this experiment is voluntary",
					type: "checkbox",
				},
				{
					text: "I understand that my data will be kept confidential and I can stop at any time without justification",
					type: "checkbox",
				}
			],
			type: "short",
		},

		{
			title: "Instructions",
			items: [
				{
					text: "You are going to be presented with different questions. For each of these <b>questions</b>, you'll have to provide an answer.", 
					type: "regular",
					variables: [],
				},
				{
					text: "",
					type: "regular",
					variables: [],
				},
				{
					text: "Feel free to take as much time as you need to answer the questions. You can increase the size of the text box by dragging down its bottom right hand corner.",
					type: "regular",
					variables :[],
				},
				{
					text: 'Please note that (very) poor quality answers, such as those composed of random characters (resulting in a nonsensical sentence) or consisting in a single repeated character  (to meet input length requirements) will potentially lead to a rejection of your submission.',
					type: 'alert',
					variables: [],
					title: "Warning"
				},

				{
					text: `You've completed <variable1> item(s) so far. <a onclick="resetState()"> Reset data?</a>`,
					type: 'info',
					variables: ['currentQuestionIndex'],
				},

			],
			type: "short",
		},
		// {
		// title: "Instructions",
		// text: "Good luck!",
		// type: "short",
		// },

	],
	questions: [
		{
			"title": "sControl",
			"text": "A scarf costs 210€ more than a hat. The scarf and the hat cost 220€ in total. How much does the hat cost?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": [''],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
		{
			"title": "sControl",
			"text": "How long would it take 80 carpenters to repair 80 tables, if it takes 8 carpenters 8 hours to repair 8 tables?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": [''],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
		{
			"title": "sControl",
			"text": "A girl has 6 balls which are either red or blue. Exactly two of these balls are blue. How many red balls does she have?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": [''],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
		{
			"title": "sControl",
			"text": "An entire forest was consumed by a wildfire in 40 hours, with its size doubling every hour. How long did it take to burn 50% of the forest?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": [''],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
		{
			"title": "sControl",
			"text": "If Andrea can clean a house in 3 hours, and Alex can clean a house in 6 hours, how many hours would it take for them to clean a house together?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": [''],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
		{
			"title": "sControl",
			"text": "A bird travels 100 miles per hour. The distance between Paris and London is 300 miles. How long would it take for the bird to go to Paris from London?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": [''],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
		{
			"title": "sControl",
			"text": "A runner participates in a marathon and arrives both at the 100th highest and the 100th lowest position. How many participants are in the marathon?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": [''],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
		{
			"title": "sControl",
			"text": "A woman buys a second-hand car for $1000, then sells it for $2000. Later she buys it back for $3000 and finally sells it for $4000. How much has she made?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": [''],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
		{
			"title": "sControl",
			"text": "Frank decided to invest $10,000 into bitcoin in January 2018. Four months after he invested, the bitcoin he had purchased went down 50%. In the subsequent eight months, the bitcoin he had purchased went up 80%. What is the value of Frank’s bitcoin after one year?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": [''],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
	],
	old_questions: [
		{
			"title": "sControl",
			"text": "A bat and a ball cost £1.10 in total. The bat costs £1.00 more than the ball. How much does the ball cost?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": ['The ball costs £0.05.'],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
		{
			"title": "sControl",
			"text": "If it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 machines to make 100 widgets?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": ['It would take 5 minutes for 100 machines to make 100 widgets.'],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
		{
			"title": "sControl",
			"text": "In a park, there are 8 trees either oaks or apple trees. Three of the trees are Oaks the others being apple trees. How many apple trees are there?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": ['There are 5 apple trees.'],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
		{
			"title": "sControl",
			"text": "In a lake, there is a patch of lily pads. Every day, the patch doubles in size. If it takes 48 days for the patch to cover the entire lake, how long would it take for the patch to cover half of the lake?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": ['The patch would require 47 days to cover half of the lake.'],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
		{
			"title": "sControl",
			"text": "If John can drink one barrel of water in 6 days, and Mary can drink one barrel of water in 12 days, how long would it take them to drink one barrel of water together?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": ['They would take 4 days to drink a barrel together.'],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
		{
			"title": "sControl",
			"text": "The distance between city A and city B is 120 miles. A car travels at 60 miles per hour. How long would it take for the car to go to city A from city B?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": ['The car would need 2 hours.'],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
		{
			"title": "sControl",
			"text": "Jerry received both the 15th highest and the 15th lowest mark in the class. How many students are in the class?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": ['There are 29 students in the class.'],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
		{
			"title": "sControl",
			"text": "A man buys a pig for £60, sells it for £70, buys it back for £80 and sells it finally for £90. How much has he made?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": ['He made £20 dollars.'],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
		{
			"title": "sControl",
			"text": "Simon decided to invest £8000 in the stock market one day early in 2008. Six months after he invested, on July 17, the stocks he had purchased went down 50%. Fortunately for Simon, from July 17 to October 17, the stocks he had purchased went up 75%. What is Simon's economic situation at this point?",
			"id": 1,
			"type": "long",
			"oldTitle": "sControl",
			"entered": ['He has £7000 at this point.'],
			"correct": "",
			"oldId": 1,
			"cond": "control",
			"dilemma": ""
		},
	]
}	