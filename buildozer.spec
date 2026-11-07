[app]

# (string) Title of your application
title = BenimHilem

# (string) Package name
package.name = benimhilem

# (string) Package domain (needed for android packaging)
package.domain = org.test

# (string) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (string) Application version
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (bool) Use fullscreenmode or not
fullscreen = 1

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21
requirements = python3==3.11.5,kivy
