# Import bcrypt:
import bcrypt

# password = "boyhandsome"
# # Encode password into a readable utf-8 byte code:
# password = password.encode('utf-8')
# # Hash the ecoded password and generate a salt:
# hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
# print(hashedPassword.decode('utf-8'))

# $2b$12$EDNCMsgfDOFuEzRCqrePxOvNWGltqh4BTiGAcOdfjUCGVP23duqfO
# passwd = b'tuancong'
# salt = bcrypt.gensalt()
# # hashed = bcrypt.hashpw(passwd, salt)
# hashed = b'$2b$12$ccw69Qz6DjQiMq1nL2JiOOHoQucc6GW3ESd5WKocoLkmE1OG4y1nW'
# if bcrypt.checkpw(passwd, hashed):
#     print("match")
# else:
#     print("does not match")

# from app.helper import Helper
# print(Helper.get_now_datetime())