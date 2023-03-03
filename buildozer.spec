[app]

title = MultimediaImage App
package.name = multimediaimageapp
package.domain = gsog.de

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3

version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a

# iOS specific
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = main
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

[buildozer]
log_level = 2
