[app]
title = BCC Control
package.name = bcccontrol
package.domain = org.ceet.bcc

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,jpeg,db
source.include_patterns = Pages/*,*.db,CEET.png

version = 1.7

# Versions compatibles et stables
requirements = python3,kivy==2.0.0,kivymd==0.104.2,pillow

# Configuration de l'icône
icon.filename = CEET.png
presplash.filename = CEET.png

# Orientation
orientation = portrait

[buildozer]
log_level = 2

[android]
# Versions compatibles qui évitent le problème AIDL
api = 30
minapi = 21
ndk = 23b
sdk = 30

# Permissions Android
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE

# Architectures
android.archs = arm64-v8a,armeabi-v7a

# Orientation
android.orientation = portrait

# Icônes
android.icon = CEET.png
android.adaptive_icon_foreground = CEET.png
android.adaptive_icon_background = #FFFFFF

# CORRECTION IMPORTANTE : Accepter automatiquement les licences
android.accept_sdk_license = True
android.skip_update = False

# Build tools version compatible
android.gradle_dependencies = 

# Configuration pour éviter les erreurs AIDL
android.add_compile_options = sourceCompatibility JavaVersion.VERSION_1_8, targetCompatibility JavaVersion.VERSION_1_8

# Désactiver les vérifications strictes
android.allow_backup = True
