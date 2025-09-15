[app]
title = BCC Control
package.name = bcccontrol  
package.domain = org.ceet.bcc
source.dir = .
source.include_exts = py,png,jpg,kv,txt
version = 1.0
requirements = python3,kivy==2.0.0
icon.filename = CEET.png
orientation = portrait

[buildozer]
log_level = 2

[android]
# Versions très stables - évitent les erreurs autotools
api = 27
minapi = 21  
ndk = 19b
sdk = 27

# Configuration simple
android.accept_sdk_license = True
android.orientation = portrait
android.icon = CEET.png
android.archs = armeabi-v7a
android.permissions = INTERNET

# Éviter les complications
android.skip_update = False
