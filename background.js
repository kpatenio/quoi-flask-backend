/* According to documentation: https://developer.chrome.com/extensions/contextMenus */
// selection context = highlighting something
// page context = anywhere on the page
var context_menu = {
  "id": "QUOI_widget",
  "title": "QUOI",
  "contexts": ["selection", "page"]
}

chrome.contextMenus.create(context_menu);

// see if our context item is selected
chrome.contextMenus.onClicked.addListener(function(clicked){
  // if highlighted a word
  if (clicked.menuItemid == "QUOI_widget" && clicked.selectionText){
    // TODO - WONT WORK! // https://stackoverflow.com/questions/17851700/how-to-open-the-default-popup-from-context-menu-in-a-chrome-extension
    //https://stackoverflow.com/questions/33361715/open-extension-popup-when-click-on-context-menu
    console.log("CLICKED");
    chrome.tabs.create({
      "url": chrome.extension.getURL('popup.html'),
      "active": false
  }, function(tab) {
      // After the tab has been created, open a window to inject the tab
      chrome.windows.create({
          "tabId": "TSET",
          "type": 'popup',
          "focused": true
      });
  });
  }
})


// TODO: use set popup : https://stackoverflow.com/a/29415742
