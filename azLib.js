// <-- AZLIBRARY PROJECT (JavaScript) -->
// Started: 2018.02.07

function getHtml(url, async=false) {
	if (window.XMLHttpRequest) {
		xmlHttp = new XMLHttpRequest();
	} else {
		xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlHttp.open("GET", url, async);
	xmlHttp.send(null);
	return xmlHttp.responseText
}