/* According to documentation: https://developer.chrome.com/extensions/contextMenus */
// selection context = highlighting something
// page context = anywhere on the page

/*
Apparently, it is not possible to open up the popup window on the browser from the contexts
menu (this is a design choice made by Google).

Sources:
 https://stackoverflow.com/questions/17851700/how-to-open-the-default-popup-from-context-menu-in-a-chrome-extension
 https://stackoverflow.com/questions/33361715/open-extension-popup-when-click-on-context-menu


 Alternate workaround - make a new window
 Content Scripts with chrome api: https://developer.chrome.com/extensions/content_scripts
 */

var contextId = "quoiContextId";

var contextMenu = {
  "id": contextId,
  "title": "QUOI",
  "contexts": ["selection", "page"]
};

// create context menu
chrome.contextMenus.create(contextMenu);

// see if our context item is selected
chrome.contextMenus.onClicked.addListener(function(clicked){

  // if highlighted a word
  if (clicked.menuItemId == contextId && clicked.selectionText){
    chrome.windows.create ({
      url : "definitions.html",
      focused : false,
      top: 200,
      left: 700,
      height: 200,
      width: 400,
      type : "popup"
    });

    // $.post('translate.yandex.net/api/v1.5/tr/getLangs?ui=en&key=trnsl.1.1.20181103T011505Z.a63896cc58809a9d.c30e5ab4e6ddf3b30c3897adb8d9675157d90a07', function(response){
    //   console.log(response);
    // });
  }


  //POST /api/v1.5/tr/getLangs?ui=en&key=API-KEY HTTP/1.1
//Host: translate.yandex.net
//Accept: */*
//Content-Type: application/x-www-form-urlencoded*/

  // else anywhere on the page
  else if (clicked.menuItemId == contextId) {
    chrome.windows.create ({
      url : "popup.html",
      focused : false,
      top: 200,
      left: 700,
      height: 200,
      width: 400,
      type : "popup"
    });
  }

}); // end of listener

// Interesting way to make a small window (not popup): https://stackoverflow.com/a/11699421

// TODO: use set popup : https://stackoverflow.com/a/29415742
