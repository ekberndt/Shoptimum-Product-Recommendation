const electron = require('electron');
const url = require('url');
const path = require('path');

const {app, BrowserWindow, Menu, MenuItem} = electron;
function loadPage(variable)
{

     window.location= variable;

}

let mainWindow;
const createWindow = () => {
  mainWindow = new BrowserWindow({width: 800, height: 600})
  mainWindow.loadURL(require('url').format({
    pathname: path.join(__dirname, 'index.html'),
    protocol: 'file:',
    slashes: true
  }))
  mainWindow.webContents.openDevTools()
  mainWindow.on('closed', () => {
    mainWindow = null
  })
}
function give_url(){
  const urls = require('url');
  var give = urls.format({
    //using url.format is a fancy way of preloading file directory as file locations can change, kind of like os.file directory import in python
      pathname: require('path').join(__dirname, '../templates/index.html'),
      protocol: 'file:', 
      slashes: true
  });
  mainWindow.loadURL(give)
};
function submit_form(){
  
  
  //append line breaks
  
  document.add_website_form.submit();
  window.location.href = "searchWindow.html";
  give_url();
  //document.getElementById("add_website_form").requestSubmit();
};
const template = [
  {
     label: 'Edit',
     submenu: [
        {
           role: 'undo'
        },
        {
           role: 'redo'
        },
        {
           type: 'separator'
        },
        {
           role: 'cut'
        },
        {
           role: 'copy'
        },
        {
           role: 'paste'
        }
     ]
  },
  
  {
     label: 'View',
     submenu: [
        {
           role: 'reload'
        },
        {
           role: 'toggledevtools'
        },
        {
           type: 'separator'
        },
        {
           role: 'resetzoom'
        },
        {
           role: 'zoomin'
        },
        {
           role: 'zoomout'
        },
        {
           type: 'separator'
        },
        {
           role: 'togglefullscreen'
        }
     ]
  },
  
  {
     role: 'window',
     submenu: [
        {
           role: 'minimize'
        },
        {
           role: 'close'
        }
     ]
  },
  
  {
     role: 'help',
     submenu: [
        {
           label: 'Learn More'
        }
     ]
  }
]

const menu = Menu.buildFromTemplate(template)
Menu.setApplicationMenu(menu)
// Listen for app to be ready
//basically the function inside app.on ready is like a lambda function, we;re defining the function for creating a window inside the parameters of app.on ready
//but not necessary
app.on('ready', function(){
    //Create new windows
    mainWindow = new BrowserWindow({});
    // Load html file in window
    mainWindow.loadURL(url.format({
      //using url.format is a fancy way of preloading file directory as file locations can change, kind of like os.file directory import in python
        pathname: path.join(__dirname, '../index.html'),
        protocol: 'file:', 
        slashes: true
    }));
    createPyProc()
});
//function definiton on app.on inside parameter definition here as well
app.on('window-all-closed', () => {
    // On macOS it is common for applications and their menu bar
    // to stay active until the user quits explicitly with Cmd + Q
    if (process.platform !== 'darwin') {
      exitPyProc()
      app.quit()
    }
  });
  //function definiton on app.on inside parameter definition here as well
  //app.on('activate', () => {
  //  if (mainWindow === null) {
  //    createWindow()
  //  }
  //  createPyProc()
  //});
  

  //adding these to end of javascript at end of js file

  let pyProc = null
  let pyPort = null
  
  const selectPort = () => {
    pyPort = 5000
    return pyPort
  }
  
  const createPyProc = () => {
    let port = '' + selectPort()
    const file_location = __dirname
    let script = "H:/python/python_repos/scalper_github_repository/main_api.py"
    pyProc = require('child_process').spawn('python', [script, port])
    if (pyProc != null) {
      console.log('child process success')
    }
  }
  
  const exitPyProc = () => {
    pyProc.kill()
    console.log('child process exit')
    pyProc = null
    pyPort = null
  }
  
  