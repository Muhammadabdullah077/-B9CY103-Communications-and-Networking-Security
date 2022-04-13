# -B9CY103-Communications-and-Networking-Security

                                             DBS students chatting app Report
	                                               End To End Encryption


Project Introduction:
			DBS chatting app is created to make a secure and table chatting web with 
Responsive UI. To implement the security of users we are using different algorithms to store passwords and with 2-factor authentication for users. We have commented on the code as well to make sure anybody else can understand it easily, to add a level of clean UI (user interface) or a solid app structure-function over a secure broadcast network we are using Bootstrap5 the latest version of bootstrap, which is an effort for a more modern approach to internet security on a communication medium. The Implementation of DBS is based on a new but effective set-up of Python Django, JavaScript, Bootstrap, and SQLite where Bootstrap is for the app structure and UI (user interface) tool, Python for the server setup, Django for better backend and to provide new technologies-based security to the App. 

Project description
PyMulticrypt
Python Module for secure End-2-End encryption using the Multicrypt algorithm made by me.

Concept behind MultiCrypt Algrorithm
So, take a number, say 77 as your message. Then, take another number, say 739 as your key (In actual, this number will be of 256 bits). Now, to get your encrypted message, just add your key to the actual message i.e. 77 + 739 in this case = 816. So your encrypted message is now 816.

Now, encrypt your key i.e. 739 in this case using RSA Encryption (Asymmetric Encryption) i.e. encrypt your key with the public key of the recipient, then append the encrypted key at the end of your encrypted message with any seperator charecter between the encrypted message and the encrypted key.

Now this message is your final encrypyed message which can be transmitted safely to the recipient.

Now when the recipient receives your encrypted message, then for decrypting that message first the recipient will seperate the actual encrypted message and the encrypted key from the seperator charecter which you used between the actual encrypted message and encrypted key at the time of encrypting the message (In actual, the seperator charecter is fixed for everyone and is equal to "K"). Then the recipient will decrypt the encrypted key using his/her private key which is mathematically linked to his/her public key.

Then the recipient gets the actual key i.e. 739 in this case. Then all he/she has to do is minus the actual key from the actual encrypted message to get the actual message i.e. 816 - 739 in this case = 77 which is the actual message which you wanted to send to the recipient.

This is highly secure as the encrypted message is safe from brute force attack. Also, no one can reverse engineer the encryption algorithm to decrypt the message as the key required to do so is encrypted asymmetrically (i.e. using RSA encryption algorithm) and everyone knows that RSA Encryption cannot be broken due to its public-private key pair system.

Hence, MultiCrypt encrypiton is a hybrid encryption algorithm (i.e. involves both symmetric encryption algorithm (key encryption) and asymmetric encryption (RSA encryption)) which is ideal for transmitting any kind of data securely using any kind of network protocol.

Please do note that I am using a cutom RSA Encryption algorithm made by me for suiting the symmetric part of the MultiCrypt algorithm. Hence, public and private keys of standard RSA Encryption System WILL NOT WORK in MultiCrypt Encryption System and vice versa.

Installation
Simply using PyPi:

pip install pymulticrypt
Usage
from pymulticrypt import End2End

e2e = End2End(Parameters)
Parameters
public_key (Optional): Public Key to be used if you want to use existing key (Default: "").
private_key (Optional): Private Key to be used if you want to use existing key (Default: "").
save (Optional): Should be True/False. Specifies whether the keys have to be stored in a file or not (Default: True).
key_path (Optional): Specifies the path and name of the file where the keys have to be stored, if save = True (Default: Same as your python file).
new (Optional): Should be True/False. Specifies whether it should ignore any existing key pairs and generate new key pair or not (Default: False).
Methods
keys()
keys = e2e.keys()
Returns Private Key and Public Key in the form of dictionary of the format {"public": %YOUR_PUBLIC_KEY%, "private": %YOUR_PRIVATE_KEY%}.

encrypt()
encrypted_message = e2e.encrypt(message, public_key)
Encrypts the message using MULTICRYPT algorithm.

Parameters

message (Required): Message to encrypt.
public_key (Required): Public Key of the recipient of the message (for the asymmetric encryption part).
decrypt()
actual_message = e2e.decrypt(message, private_key)
Decrypts the encrypted message using MULTICRYPT algorithm.

Parameters

message (Required): Encrypted Message to decryt.
private_key (Optional): Your Private Key required to decrypt any message which is encrypted with Public Key linked to that private key (Default: Key which was either passed in the End2End() constrctor or generated by the program for you).
Useful for transmitting data securely between 2 devices on a network


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


2.	FaceBook/Google Login: For social login, the PyPI package django-allauth is used. All the information is set that asked by both Google Console and Facebook developer’s console to use their authentication system. In settings.py SITE_ID is set to 1. From the Django admin panel, two separate socialProviders objects are created and they are populated by App_id and secret key that are provided by  both Google and Facebook developer consoles. Finally, in settings.py a list is created called SOCIALACCOUNT_PROVIDERS and it contains all the fields that our Django app will request, from Google and Facebook for user authentication. The URLs for social login are accessible through the link- https://dbsstudentapp.pythonanywhere.com/ 
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
