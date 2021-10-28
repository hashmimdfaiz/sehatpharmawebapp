if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("/sw.js").then(registration => {
        console.log("SW Registered!");
        console.log(registration);
    }).catch(error => {
        console.log("SW Registration Failed");
        console.log(error);
    });
}

//navigator.serviceWorker.register('', { scope: './cus_app/templates/index.html' , 'Service-Worker-Allowed':'/'})
//        .then(function (registration)
//        {
//          console.log('Service worker registered successfully');
//        }).catch(function (e)
//        {
//          console.error('Error during service worker registration:', e);
//        });