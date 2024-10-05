[app]

# Title of your application
title = Ice_cream

# Package name
package.name = Ice_cream

# Package domain (needed for android/ios packaging)
package.domain = com.ice_cream.app

# Source code where the main.py lives
source.dir = .

# Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# Application versioning
version = 0.1

# Application requirements
requirements = python3,kivy,requests,Pillow,moviepy,beautifulsoup4,google-generativeai

# Supported orientations
orientation = portrait

# Presplash of the application
 presplash.filename = %(source.dir)s/.png

# Icon of the application
 icon.filename = %(source.dir)s/.png

# (list) Permissions
android.permissions = android.permission.INTERNET,android.permission.WRITE_EXTERNAL_STORAGE

#
# Android specific
#

# Indicate if the application should be fullscreen or not
fullscreen = 1

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 23b

# Enable AndroidX support
android.enable_androidx = True

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

#
# iOS specific
#

# Path to a custom kivy-ios folder
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Whether or not to sign the code
ios.codesign.allowed = false

# Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
