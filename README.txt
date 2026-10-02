WATAPICKLE MATCHER - BUILD THE APK WITH GITHUB

Files to have in your repository (root unless noted):
  package.json, capacitor.config.json, .gitignore,
  icon.png, make_icons.py,
  www/index.html,
  .github/workflows/build-apk.yml   (paste from build-apk.yml.txt if the hidden folder won't upload)

Then: Actions tab > Build APK > Run workflow. When it is green, download
"WataPickle-Matcher-APK" from Artifacts, unzip it, uninstall the old app from your phone, and install app-debug.apk.
In the run log, the "Set app name" step should print: WataPickle Matcher.
