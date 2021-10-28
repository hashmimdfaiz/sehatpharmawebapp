//// const asset =
//self.addEventListener("install", e => {
//    e.waitUntil(
//        caches.open("static").then(cache => {
//            return cache.addAll();
//        })
//    );
//});
//self.addEventListener("fetch", e => {
//    e.respondWith(
//        caches.match(e.request).then(response => {
//            return response || fetch(e.request);
//        })
//    )
//})
var staticCacheName = 'static';

self.addEventListener('install', function(event) {
event.waitUntil(
	caches.open(staticCacheName).then(function(cache) {
	return cache.addAll(
		["/", "./fatehbhailogo.png", './images/logo.png', './images/logo1.png']
	);
	})
);
});

self.addEventListener('fetch', function(event) {
var requestUrl = new URL(event.request.url);
	if (requestUrl.origin === location.origin) {
	if ((requestUrl.pathname === '/')) {
		event.respondWith(caches.match(''));
		return;
	}
	}
	event.respondWith(
	caches.match(event.request).then(function(response) {
		return response || fetch(event.request);
	})
	);
});
