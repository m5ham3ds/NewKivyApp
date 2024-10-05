[app]
# (str) Title of your application
title = Ice_cream

# (str) Package name
package.name = Ice_cream

# (str) Package domain (needed for android/ios packaging)
package.domain = com.Ice_cream.app

# (str) Source code where the main.py file is located
source.dir = .

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# For example, to use kivy with python3:
# requirements = python3,kivy
requirements = python3,kivy,requests,Pillow,beautifulsoup4,moviepy

# (str) Custom source folders
# source.include_exts = py,png,jpg,kv,atlas

# (list) Permissions
# (list) Permissions required by the app (see android.permissions)
android.permissions = INTERNET

# (str) The format used to package the app for release mode (aab or apk).
android.release_artifact = aab

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (int) Android API to use
# android.api = 27

# (int) Minimum API required (lowest supported version)
# android.minapi = 21

# (int) Android SDK version to use
# android.sdk = 20

# (str) Full name of the main entry file
# If you use a kv file, make sure that it is located in the same directory as your main.py
# for example, if your kv file is named "myapp.kv", set this to:
# main.kv = myapp.kv
main.kv =

# (str) The name of the entry point module
# This is the main file that will be run by python-for-android to start your application
# Uncomment this line if you have a specific file to be run as the main file
# entrypoint = main.py

# (str) Android NDK version to use
# android.ndk = 20b

# (list) Add custom java compile options
# set javac options
# java.source.version = 1.8
# java.target.version = 1.8

# (bool) Indicate whether the screen should stay on
# (android only)
# android.wakelock = False

# (bool) Indicate whether to use the built-in sqlite3
# (android only)
# android.sqlite3 = True

# (list) A list of Java .jar files to add to the libs
# This is useful when you have third-party Java libraries
# that you want to include in your application
# android.add_jars = foo.jar,bar.jar,baz.jar

# (list) A list of Java .aar files to add to the libs
# This is useful when you have third-party Android Archive libraries
# that you want to include in your application
# android.add_aars = foo.aar,bar.aar,baz.aar

# (list) A list of Android modules to load
# This is useful when you have custom Java code
# that you want to include in your application
# android.add_android_modules = foo,bar,baz

# (list) A list of Android services to declare
# This is useful when you have custom Android services
# that you want to include in your application
# android.add_services = foo,bar,baz

# (str) Android packaging method
# android.packaging = "apk"

# (str) Android build mode
# android.build_mode = "release"

# (str) Android architecture to use
# android.arch = "armeabi-v7a"

# (bool) Choose whether to build with the debug keystore
# android.use_debug_keystore = True

# (str) Path to the debug keystore
# android.debug_keystore_path = ~/.android/debug.keystore

# (str) Password for the debug keystore
# android.debug_keystore_password = android

# (str) Alias for the debug keystore
# android.debug_keystore_alias = androiddebugkey

# (str) Password for the alias in the debug keystore
# android.debug_keystore_alias_password = android

# (list) A list of custom build commands
# List of (str) commands to be run during the build process
# custom.build_commands =

# (list) A list of custom build environment variables
# List of (str) environment variable assignments to be applied during the build process
# custom.build_environment =

# (str) The log level for Python logs
# log.level = "INFO"

# (str) The log level for the buildozer output
# buildozer.log.level = "INFO"

# (str) The log level for the python-for-android output
# p4a.log.level = "INFO"

# (list) A list of custom post build commands
# List of (str) commands to be run after the build process
# custom.post_build_commands =

# (list) A list of custom pre build commands
# List of (str) commands to be run before the build process
# custom.pre_build_commands =

# (bool) Whether to skip the buildozer cleanup process
# This is useful when you want to keep the build artifacts
# buildozer.cleanup = False

# (bool) Whether to use the default buildozer.spec
# This is useful when you want to use the default buildozer.spec
# buildozer.use_default = False

# (str) The path to the buildozer.spec file
# buildozer.spec =

# (list) A list of custom buildozer commands to run
# List of (str) commands to be run by buildozer
# buildozer.custom_commands =

# (bool) Whether to use the default python-for-android build
# This is useful when you want to use the default python-for-android build
# p4a.use_default = False

# (str) The path to the python-for-android build file
# p4a.build =

# (list) A list of custom python-for-android commands to run
# List of (str) commands to be run by python-for-android
# p4a.custom_commands =

# (list) A list of custom python-for-android environment variables
# List of (str) environment variable assignments to be applied during the python-for-android build process
# p4a.custom_environment =

# (bool) Whether to use the default AndroidManifest.xml
# This is useful when you want to use the default AndroidManifest.xml
# android.use_default_manifest = False

# (str) The path to the AndroidManifest.xml file
# android.manifest =

# (bool) Whether to use the default build.gradle
# android.use_default_gradle = True

# (str) The path to the build.gradle file
# android.gradle =

# (str) The path to the local.properties file
# android.local_properties =

# (bool) Whether to use the default ProGuard rules
# android.use_default_proguard = True

# (str) The path to the proguard-rules.pro file
# android.proguard =

# (list) A list of custom ProGuard rules
# List of (str) ProGuard rules to be applied
# custom.proguard_rules =

# (bool) Whether to use the default keystore
# android.use_default_keystore = True

# (str) The path to the keystore
# android.keystore =

# (str) The password for the keystore
# android.keystore_password =

# (str) The alias for the keystore
# android.keystore_alias =

# (str) The password for the alias in the keystore
# android.keystore_alias_password =

# (list) A list of custom jar files to add to the classpath
# This is useful when you have third-party Java libraries
# that you want to include in your application
# android.add_jars_to_classpath = foo.jar,bar.jar,baz.jar

# (list) A list of custom aars to add to the classpath
# This is useful when you have third-party Android Archive libraries
# that you want to include in your application
# android.add_aars_to_classpath = foo.aar,bar.aar,baz.aar

# (list) A list of custom Android modules to load
# android.add_android_modules = foo,bar,baz

# (list) A list of custom Android services to declare
# android.add_services = foo,bar,baz

# (bool) Whether to use the default Android SDK
# android.use_default_sdk = True

# (str) The path to the Android SDK
# android.sdk =

# (bool) Whether to use the default Android NDK
# android.use_default_ndk = True

# (str) The path to the Android NDK
# android.ndk =

# (bool) Whether to use the default Android toolchain
# android.use_default_toolchain = True

# (str) The path to the Android toolchain
# android.toolchain =

# (bool) Whether to use the default Android build tools
# android.use_default_build_tools = True

# (str) The path to the Android build tools
# android.build_tools =

# (bool) Whether to use the default Android platform tools
# android.use_default_platform_tools = True

# (str) The path to the Android platform tools
# android.platform_tools =

# (bool) Whether to use the default Android support libraries
# android.use_default_support_libraries = True

# (str) The path to the Android support libraries
# android.support_libraries =

# (bool) Whether to use the default Android support repository
# android.use_default_support_repository = True

# (str) The path to the Android support repository
# android.support_repository =

# (bool) Whether to use the default Android play services
# android.use_default_play_services = True

# (str) The path to the Android play services
# android.play_services =

# (bool) Whether to use the default Android firebase services
# android.use_default_firebase_services = True

# (str) The path to the Android firebase services
# android.firebase_services =

# (bool) Whether to use the default Android wear services
# android.use_default_wear_services = True

# (str) The path to the Android wear services
# android.wear_services =

# (bool) Whether to use the default Android TV services
# android.use_default_tv_services = True

# (str) The path to the Android TV services
# android.tv_services =

# (bool) Whether to use the default Android auto services
# android.use_default_auto_services = True

# (str) The path to the Android auto services
# android.auto_services =

# (bool) Whether to use the default Android instant apps
# android.use_default_instant_apps = True

# (str) The path to the Android instant apps
# android.instant_apps =

# (bool) Whether to use the default Android app bundles
# android.use_default_app_bundles = True

# (str) The path to the Android app bundles
# android.app_bundles =

# (bool) Whether to use the default Android architecture
# android.use_default_arch = True

# (str) The path to the Android architecture
# android.arch =

# (bool) Whether to use the default Android build tools version
# android.use_default_build_tools_version = True

# (str) The path to the Android build tools version
# android.build_tools_version =

# (bool) Whether to use the default Android support library version
# android.use_default_support_library_version = True

# (str) The path to the Android support library version
# android.support_library_version =

# (bool) Whether to use the default Android play services version
# android.use_default_play_services_version = True

# (str) The path to the Android play services version
# android.play_services_version =

# (bool) Whether to use the default Android firebase services version
# android.use_default_firebase_services_version = True

# (str) The path to the Android firebase services version
# android.firebase_services_version =

# (bool) Whether to use the default Android wear services version
# android.use_default_wear_services_version = True

# (str) The path to the Android wear services version
# android.wear_services_version =

# (bool) Whether to use the default Android TV services version
# android.use_default_tv_services_version = True

# (str) The path to the Android TV services version
# android.tv_services_version =

# (bool) Whether to use the default Android auto services version
# android.use_default_auto_services_version = True

# (str) The path to the Android auto services version
# android.auto_services_version =

# (bool) Whether to use the default Android instant apps version
# android.use_default_instant_apps_version = True

# (str) The path to the Android instant apps version
# android.instant_apps_version =

# (bool) Whether to use the default Android app bundles version
# android.use_default_app_bundles_version = True

# (str) The path to the Android app bundles version
# android.app_bundles_version =

# (bool) Whether to use the default Android architecture version
# android.use_default_arch_version = True

# (str) The path to the Android architecture version
# android.arch_version =

# (bool) Whether to use the default Android build tools version
# android.use_default_build_tools_version = True

# (str) The path to the Android build tools version
# android.build_tools_version =

# (bool) Whether to use the default Android support library version
# android.use_default_support_library_version = True

# (str) The path to the Android support library version
# android.support_library_version =

# (bool) Whether to use the default Android play services version
# android.use_default_play_services_version = True

# (str) The path to the Android play services version
# android.play_services_version =

# (bool) Whether to use the default Android firebase services version
# android.use_default_firebase_services_version = True

# (str) The path to the Android firebase services version
# android.firebase_services_version =

# (bool) Whether to use the default Android wear services version
# android.use_default_wear_services_version = True

# (str) The path to the Android wear services version
# android.wear_services_version =

# (bool) Whether to use the default Android TV services version
# android.use_default_tv_services_version = True

# (str) The path to the Android TV services version
# android.tv_services_version =

# (bool) Whether to use the default Android auto services version
# android.use_default_auto_services_version = True

# (str) The path to the Android auto services version
# android.auto_services_version =

# (bool) Whether to use the default Android instant apps version
# android.use_default_instant_apps_version = True

# (str) The path to the Android instant apps version
# android.instant_apps_version =

# (bool) Whether to use the default Android app bundles version
# android.use_default_app_bundles_version = True

# (str) The path to the Android app bundles version
# android.app_bundles_version =

# (bool) Whether to use the default Android architecture version
# android.use_default_arch_version = True

# (str) The path to the Android architecture version
# android.arch_version =

# (bool) Whether to use the default Android build tools version
# android.use_default_build_tools_version = True

# (str) The path to the Android build tools version
# android.build_tools_version =

# (bool) Whether to use the default Android support library version
# android.use_default_support_library_version = True

# (str) The path to the Android support library version
# android.support_library_version =

# (bool) Whether to use the default Android play services version
# android.use_default_play_services_version = True

# (str) The path to the Android play services version
# android.play_services_version =

# (bool) Whether to use the default Android firebase services version
# android.use_default_firebase_services_version = True

# (str) The path to the Android firebase services version
# android.firebase_services_version =

# (bool) Whether to use the default Android wear services version
# android.use_default_wear_services_version = True

# (str) The path to the Android wear services version
# android.wear_services_version =

# (bool) Whether to use the default Android TV services version
# android.use_default_tv_services_version = True

# (str) The path to the Android TV services version
# android.tv_services_version =

# (bool) Whether to use the default Android auto services version
# android.use_default_auto_services_version = True

# (str) The path to the Android auto services version
# android.auto_services_version =

# (bool) Whether to use the default Android instant apps version
# android.use_default_instant_apps_version = True

# (str) The path to the Android instant apps version
# android.instant_apps_version =

# (bool) Whether to use the default Android app bundles version
# android.use_default_app_bundles_version = True

# (str) The path to the Android app bundles version
# android.app_bundles_version =

# (bool) Whether to use the default Android architecture version
# android.use_default_arch_version = True

# (str) The path to the Android architecture version
# android.arch_version =

# (bool) Whether to use the default Android build tools version
# android.use_default_build_tools_version = True

# (str) The path to the Android build tools version
# android.build_tools_version =

# (bool) Whether to use the default Android support library version
# android.use_default_support_library_version = True

# (str) The path to the Android support library version
# android.support_library_version =

# (bool) Whether to use the default Android play services version
# android.use_default_play_services_version = True

# (str) The path to the Android play services version
# android.play_services_version =

# (bool) Whether to use the default Android firebase services version
# android.use_default_firebase_services_version = True

# (str) The path to the Android firebase services version
# android.firebase_services_version =

# (bool) Whether to use the default Android wear services version
# android.use_default_wear_services_version = True

# (str) The path to the Android wear services version
# android.wear_services_version =

# (bool) Whether to use the default Android TV services version
# android.use_default_tv_services_version = True

# (str) The path to the Android TV services version
# android.tv_services_version =

# (bool) Whether to use the default Android auto services version
# android.use_default_auto_services_version = True

# (str) The path to the Android auto services version
# android.auto_services_version =

# (bool) Whether to use the default Android instant apps version
# android.use_default_instant_apps_version = True

# (str) The path to the Android instant apps version
# android.instant_apps_version =

# (bool) Whether to use the default Android app bundles version
# android.use_default_app_bundles_version = True

# (str) The path to the Android app bundles version
# android.app_bundles_version =

# (bool) Whether to use the default Android architecture version
# android.use_default_arch_version = True

# (str) The path to the Android architecture version
# android.arch_version =

# (bool) Whether to use the default Android build tools version
# android.use_default_build_tools_version = True

# (str) The path to the Android build tools version
# android.build_tools_version =

# (bool) Whether to use the default Android support library version
# android.use_default_support_library_version = True

# (str) The path to the Android support library version
# android.support_library_version =

# (bool) Whether to use the default Android play services version
# android.use_default_play_services_version = True

# (str) The path to the Android play services version
# android.play_services_version =

# (bool) Whether to use the default Android firebase services version
# android.use_default_firebase_services_version = True

# (str) The path to the Android firebase services version
# android.firebase_services_version =

# (bool) Whether to use the default Android wear services version
# android.use_default_wear_services_version = True

# (str) The path to the Android wear services version
# android.wear_services_version =

# (bool) Whether to use the default Android TV services version
# android.use_default_tv_services_version = True

# (str) The path to the Android TV services version
# android.tv_services_version =

# (bool) Whether to use the default Android auto services version
# android.use_default_auto_services_version = True

# (str) The path to the Android auto services version
# android.auto_services_version =

# (bool) Whether to use the default Android instant apps version
# android.use_default_instant_apps_version = True

# (str) The path to the Android instant apps version
# android.instant_apps_version =

# (bool) Whether to use the default Android app bundles version
# android.use_default_app_bundles_version = True

# (str) The path to the Android app bundles version
# android.app_bundles_version =

# (bool) Whether to use the default Android architecture version
# android.use_default_arch_version = True

# (str) The path to the Android architecture version
# android.arch_version =

# (bool) Whether to use the default Android build tools version
# android.use_default_build_tools_version = True

# (str) The path to the Android build tools version
# android.build_tools_version =

# (bool) Whether to use the default Android support library version
# android.use_default
