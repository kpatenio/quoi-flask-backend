// Add a listener upon installation
// note that permission to use storage API is used via PERMISSIONS in manifest
chrome.runtime.onInstalled.addListener(function(){
  chrome.storage.sync.set({running:"true"}, function(){
    console.log("QUOI is currently installed and running");
  }); //TODO: see if this is necessary (ex. do we need a variable init upon installation?)
  // TODO: set up context menus following this example from Google:
  // https://github.com/GoogleChrome/chrome-app-samples/blob/master/samples/context-menu/main.js
});


// TODO: use set popup : https://stackoverflow.com/a/29415742
