import fb_auth_token
import getpass


fb_username = "your@email.com" # Enter your email here
print("Please enter your password to authorize connection")
fb_password = getpass.getpass('Password:')
fb_access_token = fb_auth_token.get_fb_access_token(fb_username, fb_password)
fb_user_id = fb_auth_token.get_fb_id(fb_access_token)
host = 'https://api.gotinder.com'

# Your real config file should simply be named "config.py"
# Just insert your fb_username and fb_password in string format
# and the fb_auth_token.py module will do the rest!
