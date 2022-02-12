AR=' Has Failed to Send Friend Request!'
AQ='Is Rate Limited'
AP='Set Bio!'
AO='Message: '
AN='Message To Send: '
AM='utf-8'
AF=' Has Sent Message!'
AE='/messages'
AD=' Is Unauthorized!'
AC=' Is Locked!'
AB='eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'
AA='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
A9='Trailers'
A8='https://discord.com/channels/@me'
A7='same-origin'
A6='cors'
A5='empty'
A4='https://discord.com'
A3='keep-alive'
A2='en-US'
A1='*/*'
A0='X-Super-Properties'
z='User-Agent'
y='TE'
x='referer'
w='sec-fetch-site'
v='sec-fetch-mode'
u='sec-fetch-dest'
t='origin'
s='DNT'
r='cookie'
q='connection'
p='accept-language'
o='accept'
n='Authorization'
m='Token Is Rate Limited'
l='https://discord.com/api/v9/channels/'
k='Token'
j='You need to verify your account'
i='Amount Is Not A Valid Number'
h=False
g=''
e=' Had An Error Code: '
d='Missing Access'
c=' Is Not Valid!'
b=' Is Phone Locked!'
a='verify'
Z='Channel ID: '
Y='Amount: '
X=int
W=range
U='content'
T='3'
S='2'
Q='Unauthorized'
P='1'
N=' - '
M=']'
K='['
L=str
I='message'
H=input
G=True
E='Token '
D='> '
C=print
from colorama import Fore as V
import asyncio as O,os as R,requests as J,emoji
from Variables import ShowTokensLoaded as AG,AsciiFont as AH,RemoveTokens as F
A=V.LIGHTBLUE_EX
f=V.LIGHTRED_EX
AI=V.LIGHTMAGENTA_EX
B=V.WHITE
class AJ:
	def __init__(A):
		A.TokensFile=open('tokens.txt','r');A.ReadTokens=A.TokensFile.readlines();A.tokens=[]
		for B in A.ReadTokens:A.tokens.append(B)
	async def Logo(E):
		G='█';F='--------------------------';D='-';R.system('cls;clear');C('Made With '+AI+'</3 '+B+'By StvnedEagle');C(F.replace(D,A+D+f+D));C('██╗  ██╗ █████╗ ██████╗ ███████╗███████╗\n██║  ██║██╔══██╗██╔══██╗██╔════╝██╔════╝\n███████║███████║██║  ██║█████╗  ███████╗\n██╔══██║██╔══██║██║  ██║██╔══╝  ╚════██║\n██║  ██║██║  ██║██████╔╝███████╗███████║\n╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝'.replace(G,A+G+f))
		if AG:C(A+L(len(E.tokens))+' Tokens Loaded ')
		C(F.replace(D,A+D+f+D))
	async def MainMenu(D):
		await D.Logo();C(A+K+B+P+A+M+B+N+A+'Common');C(A+K+B+S+A+M+B+N+A+'Extra');C(A+K+B+T+A+M+B+N+A+'Token Utils');E=H()
		if E.__eq__(P):await D.CommonCategory()
		if E.__eq__(S):await D.ExtraCategory()
		if E.__eq__(T):await D.UtilsCategory()
	def CensorToken(A,O00000OOOO0OO000O):return L(O00000OOOO0OO000O[:24]+g*34)+' '
	def GrabHeaders(B,OO0OO0OOO0OOOO00O):
		A=OO0OO0OOO0OOOO00O
		try:return{n:L(A,AM),o:A1,p:A2,q:A3,r:f"__cfduid={R.urandom(43).hex()}; __dcfduid={R.urandom(32).hex()}; locale=en-US",s:P,t:A4,u:A5,v:A6,w:A7,x:A8,y:A9,z:AA,A0:AB}
		except:return{n:A,o:A1,p:A2,q:A3,r:f"__cfduid={R.urandom(43).hex()}; __dcfduid={R.urandom(32).hex()}; locale=en-US",s:P,t:A4,u:A5,v:A6,w:A7,x:A8,y:A9,z:AA,A0:AB}
	async def CommonCategory(E):
		W='5';V='4';await E.Logo();C(A+D+B+'Joiner and Leaver coming soon');C(A+K+B+P+A+M+B+N+A+'Channel Spammer');C(A+K+B+S+A+M+B+N+A+'Typing Spammer');C(A+K+B+T+A+M+B+N+A+'DM Spammer');C(A+K+B+V+A+M+B+N+A+'Friend Spammer');C(A+K+B+W+A+M+B+N+A+'Reaction Spammer');I=H()
		if I.__eq__(P):
			L=H(A+D+B+Y+A)
			if L.isdigit()==h:G=C(A+D+B+i);await O.sleep(2);await E.CommonCategory()
			G=H(A+D+B+AN+A);J=H(A+D+B+Z+A)
			for F in E.tokens:await E.ChatSpammer(F,G,J,L)
			await E.CommonCategory()
		elif I.__eq__(S):
			J=H(A+D+B+Z+A)
			for F in E.tokens:await E.TypingSpammer(F,J)
			await O.sleep(2);await E.CommonCategory()
		elif I.__eq__(T):
			G=H(A+D+B+AO+A);J=H(A+D+B+'User ID: '+A);L=H(A+D+B+Y+A)
			for F in E.tokens:await E.DMSpammer(F,J,G,L)
			await O.sleep(2);await E.CommonCategory()
		elif I.__eq__(V):
			C(A+D+B+'Name & Discrim. Example: (stoned.eagle#0001)');Q=H()
			for F in E.tokens:await E.FriendSpammer(F,Q)
			await O.sleep(2);await E.CommonCategory()
		elif I.__eq__(W):
			R=H(A+D+B+Z+A);G=H(A+D+B+'Message ID: '+A);U=H(A+D+B+'Emoji'+A)
			for F in E.tokens:await E.ReactionAdder(F,R,G,U)
			await O.sleep(2);await E.CommonCategory()
	async def UtilsCategory(E):
		L='Text: ';await E.Logo();C(A+K+B+P+A+M+B+N+A+'Set Tokens Bio');C(A+K+B+S+A+M+B+N+A+'Set Tokens Status');I=H()
		if I.__eq__(P):
			F=H(A+D+B+L+A)
			for G in E.tokens:await E.BioChanger(G,F)
			await E.UtilsCategory()
		if I.__eq__(S):
			F=H(A+D+B+L+A);J=H(A+D+B+'Emoji (Example:😋) (Leave Blank For None)'+A)
			for G in E.tokens:await E.StatusChanger(G,F,J)
			await E.UtilsCategory()
	async def BioChanger(H,OOO0O0OOO000OO0OO,O0OOO0OO000O0000O):
		K=O0OOO0OO000O0000O;I=OOO0O0OOO000OO0OO;M=H.GrabHeaders(I);N={'bio':K};L=J.patch('https://discord.com/api/v9/users/@me',headers=M,json=N)
		if L.status_code==200:C(A+D+B+E+H.CensorToken(I)+AP)
		elif L.status_code==429:C(A+D+B+E+H.CensorToken(I)+AQ)
		else:
			K=L.text
			if j in K:
				C(A+D+B+E+H.CensorToken(I)+AC)
				if I in H.tokens and F==G:H.tokens.remove(I)
			elif Q in K:
				C(A+D+B+E+H.CensorToken(I)+AD)
				if I in H.tokens and F==G:H.tokens.remove(I)
			else:C(A+D+B+k+H.CensorToken(I)+AR)
	async def StatusChanger(H,OO0O000000O0OO0OO,OOO00O0O0O0OO0OOO,O0OO0OO00O0OO0OOO):
		M=OOO00O0O0O0OO0OOO;I=OO0O000000O0OO0OO;N=H.GrabHeaders(I);P={'custom_status':{'text':M,'emoji_name':O0OO0OO00O0OO0OOO}};K=J.patch('https://discord.com/api/v9/users/@me/settings',headers=N,json=P)
		if K.status_code==200 or K.status_code==204:C(A+D+B+E+H.CensorToken(I)+AP)
		elif K.status_code==429:C(A+D+B+E+H.CensorToken(I)+AQ)
		else:
			C(L(K.status_code));await O.sleep(5);M=K.text
			if j in M:
				C(A+D+B+E+H.CensorToken(I)+AC)
				if I in H.tokens and F==G:H.tokens.remove(I)
			elif Q in M:
				C(A+D+B+E+H.CensorToken(I)+AD)
				if I in H.tokens and F==G:H.tokens.remove(I)
			else:C(L(K.status_code));await O.sleep(5)
	async def ExtraCategory(E):
		await E.Logo();C(A+K+B+P+A+M+B+N+A+'Ascii Spammer');C(A+K+B+S+A+M+B+N+A+'Lag Message Spammer');C(A+K+B+T+A+M+B+N+A+'Webhook Spammer');I=H()
		if I.__eq__(P):
			F=H(A+D+B+Y+A)
			if F.isdigit()==h:G=C(A+D+B+i);await O.sleep(2);await E.ExtraCategory()
			G=H(A+D+B+AN+A);J=H(A+D+B+Z+A)
			for L in E.tokens:await E.AsciiSpam(L,G,J,F)
			await E.ExtraCategory()
		if I.__eq__(S):
			F=H(A+D+B+Y+A)
			if F.isdigit()==h:C(A+D+B+i);await O.sleep(2);await E.ExtraCategory()
			J=H(A+D+B+Z+A)
			for L in E.tokens:await E.LagSpammer(L,J,F)
			await E.ExtraCategory()
		if I.__eq__(T):
			F=H(A+D+B+Y+A)
			if F.isdigit()==h:C(A+D+B+i);await O.sleep(2);await E.ExtraCategory()
			Q=H(A+D+B+'Webhook: '+A);G=H(A+D+B+AO+A);await E.WebhookSpammer(Q,G,F);await E.ExtraCategory()
	async def WebhookSpammer(H,OOOO00O00OOO0OO0O,O000OO0O0OO00O00O,O0O0000O0O0O0OOOO):
		F={o:A1,p:A2,q:A3,r:f"__cfduid={R.urandom(43).hex()}; __dcfduid={R.urandom(32).hex()}; locale=en-US",s:P,t:A4,u:A5,v:A6,w:A7,x:A8,y:A9,z:AA,A0:AB};G={U:O000OO0O0OO00O00O}
		for I in W(X(O0O0000O0O0O0OOOO)):
			E=J.post(OOOO00O00OOO0OO0O,headers=F,json=G)
			if E.status_code==429:C(A+D+B+'Rate Limited')
			elif E.status_code==200 or E.status_code==204:C(A+D+B+'Sent Message!')
	async def LagSpammer(H,O00O00OOOO0OO0000,O000O0O0OOOOOOOOO,OOO0OOO0O00O00O00):
		K=O00O00OOOO0OO0000;O=H.GrabHeaders(K);P={U:'你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗吗你能肯定吗你能肯定吗你能肯定吗你能肯定吗你'}
		for R in W(X(OOO0OOO0O00O00O00)):
			M=J.post(l+O000O0O0OOOOOOOOO+AE,headers=O,json=P)
			if M.status_code==429:C(A+D+B+m)
			elif M.status_code==200 or M.status_code==204:C(A+D+B+E+H.CensorToken(K)+AF)
			else:
				C(L(M.status_code));N=M.json()
				if I in N:
					if a in N[I]:
						C(A+D+B+E+H.CensorToken(K)+b)
						if K in H.tokens and F==G:H.tokens.remove(K)
					elif Q in N[I]:
						C(A+D+B+E+H.CensorToken(K)+c)
						if K in H.tokens and F==G:H.tokens.remove(K)
						if K in H.tokens and F==G:H.tokens.remove(K)
					elif d in N[I]:0
					else:
						C(A+D+B+E+H.CensorToken(K)+e+L(M.status_code))
						if K in H.tokens and F==G:H.tokens.remove(K)
	async def FriendSpammer(H,O00O0O0OO0OO0O00O,O00000000O00O0000):
		R='#';L=O00000000O00O0000;I=O00O0O0OO0OO0O00O;N=L.split(R)[0];O=L.split(R)[1];P=H.GrabHeaders(I);K=J.post('https://discord.com/api/v9/users/@me/relationships',json={'discriminator':O,'username':N},headers=P)
		if K.status_code==204:C(A+D+B+E+H.CensorToken(I)+'Friended User!')
		elif K.status_code==400:C(A+D+B+E+H.CensorToken(I)+'Invalid User!')
		else:
			M=K.text
			if j in M:
				C(A+D+B+E+H.CensorToken(I)+AC)
				if I in H.tokens and F==G:H.tokens.remove(I)
			elif Q in M:
				C(A+D+B+E+H.CensorToken(I)+AD)
				if I in H.tokens and F==G:H.tokens.remove(I)
			else:C(A+D+B+k+H.CensorToken(I)+AR)
	async def DMSpammer(H,O0000OO0O0000OOOO,OOOO0000OOOOOO0O0,O00OOO0O00O000000,amount=P):
		I=O0000OO0O0000OOOO;N=H.GrabHeaders(I)
		for R in W(X(amount)):
			K=J.post('https://discord.com/api/v9/users/@me/channels',headers=N,json={'recipient_id':OOOO0000OOOOOO0O0})
			if K.status_code==200:
				O=K.json();P=O['id'];M=J.post('https://discord.com/api/v9/channels/%s/messages'%P,headers=N,json={U:O00OOO0O00O000000});M=K.text
				if U in M:C(A+D+B+k+H.CensorToken(I)+' Has sent the message!')
				elif j in M:
					C(A+D+B+k+H.CensorToken(I)+'Locked Account!')
					if I in H.tokens and F==G:H.tokens.remove(I)
				elif Q in M:C(A+D+B+E+H.CensorToken(I)+' Invalid Token!')
				elif K.status_code==200:C(A+D+B+E+H.CensorToken(I)+' Sent Message!')
			else:C(A+D+B+E+H.CensorToken(I)+' Failed To Send!'+L(K.status_code))
	async def ReactionAdder(H,OOOO0O00O00OO000O,OO000OO00OO000O00,OOO0O00OOO000OOOO,O00O000OOO0O0O0O0):
		K=OOOO0O00O00OO000O;O=H.GrabHeaders(K);P=emoji.emojize(O00O000OOO0O0O0O0,use_aliases=G);M=J.put('https://discord.com/api/v8/channels/'+OO000OO00OO000O00+'/messages/'+OOO0O00OOO000OOOO+'/reactions/'+P+'/@me',headers=O)
		if M.status_code==429:C(A+D+B+m)
		elif M.status_code==204:C(A+D+B+E+H.CensorToken(K)+' Has Reacted To Message!')
		else:
			N=M.json()
			if I in N:
				if a in N[I]:
					C(A+D+B+E+H.CensorToken(K)+b)
					if K in H.tokens and F==G:H.tokens.remove(K)
				elif Q in N[I]:
					C(A+D+B+E+H.CensorToken(K)+c)
					if K in H.tokens and F==G:H.tokens.remove(K)
					if K in H.tokens and F==G:H.tokens.remove(K)
				elif d in N[I]:0
				else:
					C(A+D+B+E+H.CensorToken(K)+e+L(M.status_code))
					if K in H.tokens and F==G:H.tokens.remove(K)
	async def ChatSpammer(H,OO0OOO0O0O0O00O0O,O000OO00O0O0O0O00,O00O00OO0OOOO0O00,OO000000OOOOO0OO0):
		K=OO0OOO0O0O0O00O0O;O=H.GrabHeaders(K);P={U:O000OO00O0O0O0O00}
		for R in W(X(OO000000OOOOO0OO0)):
			M=J.post(l+O00O00OO0OOOO0O00+AE,headers=O,json=P)
			if M.status_code==429:C(A+D+B+m)
			elif M.status_code==200:C(A+D+B+E+H.CensorToken(K)+AF)
			else:
				N=M.json()
				if I in N:
					if a in N[I]:
						C(A+D+B+E+H.CensorToken(K)+b)
						if K in H.tokens and F==G:H.tokens.remove(K)
					elif Q in N[I]:
						C(A+D+B+E+H.CensorToken(K)+c)
						if K in H.tokens and F==G:H.tokens.remove(K)
						if K in H.tokens and F==G:H.tokens.remove(K)
					elif d in N[I]:0
					else:
						C(A+D+B+E+H.CensorToken(K)+e+L(M.status_code))
						if K in H.tokens and F==G:H.tokens.remove(K)
	async def AsciiSpam(H,O000OO0OO0O0OOOO0,OO0O00OO00OO0O0O0,O0O0000OO0000O0OO,O000000O0000OO00O):
		V='```';K=O000OO0OO0O0OOOO0;import urllib.request;O=H.GrabHeaders(K);P='https://artii.herokuapp.com/make?text='+OO0O00OO00OO0O0O0+'&font='+AH;R=urllib.request.urlopen(P);S=R.read();T={U:V+L(S,AM)+V}
		for Y in W(X(O000000O0000OO00O)):
			M=J.post(l+O0O0000OO0000O0OO+AE,headers=O,json=T)
			if M.status_code==429:C(A+D+B+m)
			elif M.status_code==200:C(A+D+B+E+H.CensorToken(K)+AF)
			else:
				N=M.json()
				if I in N:
					if a in N[I]:
						C(A+D+B+E+H.CensorToken(K)+b)
						if K in H.tokens and F==G:H.tokens.remove(K)
					elif Q in N[I]:
						C(A+D+B+E+H.CensorToken(K)+c)
						if K in H.tokens and F==G:H.tokens.remove(K)
						if K in H.tokens and F==G:H.tokens.remove(K)
					elif d in N[I]:0
					else:C(A+D+B+E+H.CensorToken(K)+e+L(M.status_code))
	async def TypingSpammer(K,OO0OO0OO0O000000O,O00OO000000O0OO0O):
		H=OO0OO0OO0O000000O;O={n:H.replace('\n',g).replace("b'",g).replace("'",g)};M=J.post(l+O00OO000000O0OO0O+'/typing',headers=O)
		if M.status_code==400:C(A+D+B+'Token Couldnt Type')
		elif M.status_code==204:C(A+D+B+E+K.CensorToken(H)+' Has Started Typing!')
		else:
			N=M.json()
			if I in N:
				if a in N[I]:
					C(A+D+B+E+K.CensorToken(H)+b)
					if H in K.tokens and F==G:K.tokens.remove(H)
				elif Q in N[I]:
					C(A+D+B+E+K.CensorToken(H)+c)
					if H in K.tokens and F==G:K.tokens.remove(H)
					if H in K.tokens and F==G:K.tokens.remove(H)
				elif d in N[I]:0
				else:
					C(A+D+B+E+K.CensorToken(H)+e+L(M.status_code))
					if H in K.tokens and F==G:K.tokens.remove(H)
import time
AS=J.get('https://icanhazip.com')
AT=J.get('https://raw.githubusercontent.com/StvnedEagle1337/Stuff/main/Auth.txt')
AK=AJ()
AL=O.get_event_loop()
AL.run_until_complete(AK.MainMenu())