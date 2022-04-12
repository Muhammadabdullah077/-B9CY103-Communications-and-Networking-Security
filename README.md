# -B9CY103-Communications-and-Networking-Security

                                             DBS students chatting app Report
	                                               End To End Encryption


Project Introduction:
			DBS chatting app is created to make a secure and table chatting web with 
Responsive UI. To implement the security of users we are using different algorithms to store passwords and with 2-factor authentication for users. We have commented on the code as well to make sure anybody else can understand it easily, to add a level of clean UI (user interface) or a solid app structure-function over a secure broadcast network we are using Bootstrap5 the latest version of bootstrap, which is an effort for a more modern approach to internet security on a communication medium. The Implementation of DBS is based on a new but effective set-up of Python Django, JavaScript, Bootstrap, and SQLite where Bootstrap is for the app structure and UI (user interface) tool, Python for the server setup, Django for better backend and to provide new technologies-based security to the App. 

Aims and Objectives:
 			Just like other social apps, you have a list of conversations with all users, that you’re engaged in. our objective is to make it more secure, and we have tried our best to make it better and secure by adding Email Verification, user Authentication, user Authorizations (as Django handles it in a very good manner) and Password’s security. we are using SHA256 hash to secure our password that is stored in our database.

Technologies and Dependencies we are using:
 						We are Using Python and Django for DBS Chatting App. We used DRF and JavaScript to make it more perfect and scalable.

Language:
1.	Backend:
a.	Python
i.	:
1.	We are using Python best web Framework to create Chatting app 
2.	Toolkit:
a.	We are using Django Toolkit for creating rest Api’s for messages.
2.	Frontend:
a.	Html
b.	CSS
c.	Bootstrap5 for responsiveness
d.	JavaScript to make app as a single page in chatting and messaging work.

Security Work:



1.	EndToEnd Encryption: The PyPI package called PyMulticrypt is used for applying an end-to-end encryption effect on the messages sent by users of the system. When a user types a message and clicks the send button from a browser, the inputted data is serialized and the message field is grabbed and it is encrypted by the function. Then an end-to-end class is initialized-


e2e =End2End(save=False)
Now the actual text message that was inputted by a requesting user, is passed to e2e.ecnrypt() function along with a public key. The message model contains a text field called, private_key that will be used later by the receiving user for decrypting the message. Now the data are passed to MessageSerializer and it is saved in the database. 

Now if the admin visits the admin panel he/she won’t be able to see the actual text message that was sent by the users.


2.	FaceBook/Google Login: For social login, the PyPI package django-allauth is used. All the information is set that asked by both Google Console and Facebook developer’s console to use their authentication system. In settings.py SITE_ID is set to 1. From the Django admin panel, two separate socialProviders objects are created and they are populated by App_id and secret key that are provided by  both Google and Facebook developer consoles. Finally, in settings.py a list is created called SOCIALACCOUNT_PROVIDERS and it contains all the fields that our Django app will request, from Google and Facebook for user authentication. The URLs for social login are accessible through the link- “https://dbsstudentapp.pythonanywhere.com/accounts/login/”
3.	PBKDF2 Algorithm:
a.	For Users Authentication we are using PBKDF2 algorithm with a SHA256 hash, a password stretching mechanism recommended by NIST. This should be sufficient for most users: it's quite secure, requiring massive amounts of computing time to break.

4.	Authentication:
a.	we are using Django built int users’ authentication and authorization functionalities. It is based on Django Session Framework. Which helps to make authorization easy and making login secure instead of doing it manually.

5.	Authorization:
a.	We are using Django Users Management to authorize Admin and other staff users as well. By this no body gets extra or less rights to do in web app, like:
i.	Users Management 
ii.	Messages App Management

6.	Two Factor Authentication:
a.	To make sure about user authentication we have added extra layer of security as 2 factor authentication by email. Whenever user signup or register for the first time he has to add the email verification code that is sent by our Django App.
b.	Otherwise, user can see the message and form to verify first and then can chat to other users

Now the actual text message that was inputted by a requesting user, is passed to e2e.ecnrypt() function along with a public key. The message model contains a text field called, private_key that will be used later by the receiving user for decrypting the message. Now the data are passed to MessageSerializer and it is saved in the database. 

Now if the admin visits the admin panel he/she won’t be able to see the actual text message that was sent by the users.


Use case Table:


Level 0	Level 1	Level 2	actor


Chat application	

Authentication system	
Register Login logout	
user
Chat
application	Chat form	Send message	
user
Chat
application	
maintenance	User’s profile
Data base	
admin





Requirements Specifications:

NAME	FUNCT IONAL	DESCRIPTION
User
registration	Yes	Functionality for user to create account
Login	Yes	Functionality for user to get access
Logout	Yes	Functionality for user to delete session
Send message	Yes	To send message
Reliability		Trusted by users
Supportability		Being supportive
portability		Application runs in different systems
 
Authentication Service:







Live Testing:
		We have tested it on PythonAnywhere.com as well it’s providing us a free 3 months hosting space to test the things on it.
Live Website Link:  
                                            https://dbsstudentapp.pythonanywhere.com/       
