[app]
title = BCC Control
package.name = bcccontrol  
package.domain = org.ceet.bcc
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,jpeg,db
version = 1.7
requirements = python3,kivy
icon.filename = CEET.png
presplash.filename = CEET.png
orientation = portrait

[buildozer]
log_level = 2

[android]
# Versions simples et stables
api = 27
minapi = 21
ndk = 17c
sdk = 27

# Permissions de base
android.permissions = INTERNET

# Orientation forcée en vertical
android.orientation = portrait

# Logo/Icône
android.icon = CEET.png

# Acceptation automatique des licences
android.accept_sdk_license = True
android.skip_update = False

# Architecture simple
android.archs = armeabi-v7a
