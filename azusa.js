// <-- AZUSA PROJECT (JavaScript) -->
// Started: 2018.02.07
// Latest: 2018.04.17

// !-- Some functions need jquery!!

// =========================
// |  Avaliable functions  |
// =========================
// cookieWrite(key, value)
// cookieGet(key)
// randomStr(length, symbol=true)
// xssAvoid(rawStr)
// notificationPermissionRequest()
// notificationShow(title, showText)

function cookieWrite(key, value) {
	document.cookie = `${key}=${value}`;
}
function cookieGet(key) {
	var arr, reg = new RegExp("(^| )"+key+"=([^;]*)(;|$)");
	if (arr = document.cookie.match(reg)) {
		return unescape(arr[2]);
	} else {
		return null;
	}
}


function randomStr(length, symbol=true) {
	var gen = '';
	if (symbol) {
		var charLib = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=|';
	} else {
		var charLib = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
	}
	
	for (var i=0; i<length; i++) {
		index = Math.round(Math.random() * (charLib.length - 1));
		gen += charLib[index];
	}
	return gen;
}


function xssAvoid(rawStr){
	return rawStr.replace(/</g, '&lt').replace(/>/g, '&gt');
}


function notificationPermissionRequest() {
	if (Notification.permission === "default") {
		Notification.requestPermission();
	}
}
function notificationShow(title, showText) {
	if(document.hidden && Notification.permission === "granted" && notice) {
		var notification = new Notification(title, {
			body: showText,
		});
		notification.onclick = function() {
			window.focus();
		};
	}
}


// var box_text = {
// // -------------------
// // Text1
// // Text2
// // ...
// // -------------------
// // This function requests jquery
// 	text: [],
// 	color_text: [],
// 	color_background: 'white',
// 	width: '100%',

// 	boxInsert: function (elementId) {
// 		var box = ``;
// 	}
// }

var imgWall = {

	u_height: 128,
	u_width: 128,
	units: [],
	
	addNew: function (src, url, text) {
		this.units.push([src, url, text]);
	},
	
	draw: function (elementId) {
		var sw;
		if (this.u_width * this.units.length > $(window).width()) {
			sw = $(window).width();
		} else {
			sw = this.u_width * this.units.length
		}
		var col = (sw / this.u_width);
		
		$(`#${elementId}`).html(`<table width="${sw}px" id="iwMain" border="0"></table>`);
		
		for (var r=0;;r++) {
			$('#iwMain').append(`<tr id="iw_ir${r}"></tr>\n<tr id="iw_tr${r}"></tr>`);
			for (var c=0; c<col; c++) {
				var u_cur = this.units.pop();
				$(`#iw_ir${r}`).append(`<td><a href="${u_cur[1]}" target="_blank"><img src="${u_cur[0]}" width="${this.u_width}px" height="${this.u_height}px"></td>`);
				$(`#iw_tr${r}`).append(`<td width="${this.u_width}px"><a href="${u_cur[1]}" target="_blank">${u_cur[2]}</td>`);
			}
			if (this.units.length === 0) {
				break;
			}
		}
	},
}
