# -*- coding: utf-8 -*-

"""
2016 MegCgo Full Stack Developer

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>

"""

import urllib, urllib2, sys, re, os, unicodedata
import xbmc, xbmcgui, xbmcplugin, xbmcaddon

plugin_handle = int(sys.argv[1])

mysettings = xbmcaddon.Addon(id = 'plugin.video.info-tv-pobres')
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
lng = xbmcaddon.Addon().getLocalizedString

xml_regex = '<title>(.*?)</title>\s*<link>(.*?)</link>\s*<thumbnail>(.*?)</thumbnail>'
m3u_thumb_regex = 'tvg-logo=[\'"](.*?)[\'"]'
m3u_regex = '#(.+?),(.+)\s*(.+)\s*'

u_tube = 'http://www.youtube.com'


def removeAccents(s):
	return ''.join((c for c in unicodedata.normalize('NFD', s.decode('utf-8')) if unicodedata.category(c) != 'Mn'))
					
def read_file(file):
    try:
        f = open(file, 'r')
        content = f.read()
        f.close()
        return content
    except:
        pass

def pobres(pobres):
	result = "u" + "g" * 2 + "cf:" + "/" * 2 + "qy.qebcobkhfrepbagrag.pbz/f/" + pobres + ".z3h?enj=1"
	return result.decode('rot13')

def make_request(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36')
		response = urllib2.urlopen(req)	  
		link = response.read()
		response.close()  
		return link
	except urllib2.URLError, e:
		print 'We failed to open "%s".' % url
		if hasattr(e, 'code'):
			print 'We failed with error code - %s.' % e.code	
		if hasattr(e, 'reason'):
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason
			
def catstyle(nome):
	return '» ' + nome + ' [COLOR white][B]>[/B][/COLOR]'

def trans(id):
	return lng(id).encode('utf-8')

full = pobres('y3zo8c74hx84jvr/vcgi-qbf-cboerf')

animacao_fanart = xbmc.translatePath(os.path.join(home, 'resources/media/animacao_fanart.jpg'))
animacao_icon = xbmc.translatePath(os.path.join(home, 'resources/media/animacao_icon.png'))
animacao = pobres('ylhsnn1h03bv45l/vcgi-cboerf-Navznpnb')

brasil_fanart = xbmc.translatePath(os.path.join(home, 'resources/media/brasil_fanart.jpg'))
brasil_icon = xbmc.translatePath(os.path.join(home, 'resources/media/brasil_icon.png'))
brasil = pobres('fcxeiwunml71gef/vcgi-cboerf-Oenfvy')

cameras_fanart = xbmc.translatePath(os.path.join(home, 'resources/media/cameras_fanart.jpg'))
cameras_icon = xbmc.translatePath(os.path.join(home, 'resources/media/cameras_icon.png'))
cameras = pobres('jiktq0z13eltdhk/vcgi-cboerf-Pnzrenf')

desporto_fanart = xbmc.translatePath(os.path.join(home, 'resources/media/desporto_fanart.jpg'))
desporto_icon = xbmc.translatePath(os.path.join(home, 'resources/media/desporto_icon.png'))
desporto = pobres('iywpgiguau3dx4v/vcgi-cboerf-Qrfcbegb')

espanha_fanart = xbmc.translatePath(os.path.join(home, 'resources/media/espanha_fanart.jpg'))
espanha_icon = xbmc.translatePath(os.path.join(home, 'resources/media/espanha_icon.png'))
espanha = pobres('0218gwot12h9fh4/vcgi-cboerf-Rfcnaun')

franca_fanart = xbmc.translatePath(os.path.join(home, 'resources/media/franca_fanart.jpg'))
franca_icon = xbmc.translatePath(os.path.join(home, 'resources/media/franca_icon.png'))
franca = pobres('zck3tzsoemhskr5/vcgi-cboerf-Senapn')

italia_fanart = xbmc.translatePath(os.path.join(home, 'resources/media/italia_fanart.jpg'))
italia_icon = xbmc.translatePath(os.path.join(home, 'resources/media/italia_icon.png'))
italia = pobres('9tdo3mz9dpgjhim/vcgi-cboerf-Vgnyvn')

musica_fanart = xbmc.translatePath(os.path.join(home, 'resources/media/musica_fanart.jpg'))
musica_icon = xbmc.translatePath(os.path.join(home, 'resources/media/musica_icon.png'))
musica = pobres('ho4e1h15a95bcok/vcgi-cboerf-Zhfvpn')

portugal_fanart = xbmc.translatePath(os.path.join(home, 'resources/media/portugal_fanart.jpg'))
portugal_icon = xbmc.translatePath(os.path.join(home, 'resources/media/portugal_icon.png'))
portugal = pobres('nqpfoh14sij15dy/vcgi-cboerf-Cbeghtny')

usa_fanart = xbmc.translatePath(os.path.join(home, 'resources/media/usa_fanart.jpg'))
usa_icon = xbmc.translatePath(os.path.join(home, 'resources/media/usa_icon.png'))
usa = pobres('muepfje6iy67nhc/vcgi-cboerf-HFN')

temp_fanart = xbmc.translatePath(os.path.join(home, 'resources/media/temp_fanart.jpg'))
temp_icon = xbmc.translatePath(os.path.join(home, 'resources/media/temp_icon.png'))
temp = pobres('2cfr94gh94f2x27/vcgi-cboerf-Grzc')

radios_fanart = xbmc.translatePath(os.path.join(home, 'resources/media/radios_fanart.jpg'))
radios_icon = xbmc.translatePath(os.path.join(home, 'resources/media/radios_icon.png'))
radios = pobres('no5zkuupgttuv3x/vcgi-cboerf-Enqvbf')

world_fanart = xbmc.translatePath(os.path.join(home, 'resources/media/world_fanart.jpg'))
world_icon = xbmc.translatePath(os.path.join(home, 'resources/media/world_icon.png'))
world = pobres('2bxjap8tapw9dle/vcgi-cboerf-jbeyq')

def main():
	add_dir('[COLOR white][B]>[/B][/COLOR] [I]' + trans(33002) + '[/I]  [COLOR white][B]>>[/B][/COLOR]', 'searchlink', 99, icon, fanart)
#	if len(full) > 0:
#		add_dir('[COLOR white]Lista Total [B]>>[/B][/COLOR]', u_tube, 2, icon, fanart)
	if len(animacao) > 0:
		add_dir(catstyle(trans(33003)), u_tube, 3, animacao_icon, animacao_fanart)
	if len(brasil) > 0:
		add_dir(catstyle(trans(33004)), u_tube, 4, brasil_icon, brasil_fanart)
	if len(cameras) > 0:
		add_dir(catstyle(trans(33005)), u_tube, 5, cameras_icon, cameras_fanart)
	if len(desporto) > 0:
		add_dir(catstyle(trans(33006)), u_tube, 6, desporto_icon, desporto_fanart)
	if len(espanha) > 0:
		add_dir(catstyle(trans(33007)), u_tube, 7, espanha_icon, espanha_fanart)
	if len(franca) > 0:
		add_dir(catstyle(trans(33008)), u_tube, 8, franca_icon, franca_fanart)
	if len(italia) > 0:
		add_dir(catstyle(trans(33009)), u_tube, 9, italia_icon, italia_fanart)
	if len(musica) > 0:
		add_dir(catstyle(trans(33010)), u_tube, 10, musica_icon, musica_fanart)
	if len(portugal) > 0:
		add_dir(catstyle(trans(33011)), u_tube, 11, portugal_icon, portugal_fanart)
	if len(usa) > 0:
		add_dir(catstyle(trans(33012)), u_tube, 12, usa_icon, usa_fanart)
	if len(temp) > 0:
		add_dir(catstyle(trans(33013)), u_tube, 13, temp_icon, temp_fanart)
	if len(world) > 0:
		add_dir(catstyle(trans(33014)), u_tube, 14, world_icon, world_fanart)
	if len(radios) > 0:
		add_dir(catstyle(trans(33020)), u_tube, 20, radios_icon, radios_fanart)

	"""
	if (len(full) < 1 and len(animacao) < 1 and len(online_xml) < 1 and len(local_xml) < 1 ):
		mysettings.openSettings()
	
	xbmc.executebuiltin("Container.Refresh")
	"""

def search(): 	
	try:
		keyb = xbmc.Keyboard('', trans(33001))
		keyb.doModal()
		if (keyb.isConfirmed()):
			searchText = urllib.quote_plus(keyb.getText()).replace('+', ' ')
#		if len(full) > 0:		
#			content = make_request(full)
#			match = re.compile(m3u_regex).findall(content)
#			for thumb, name, url in match:
#				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
#					m3u_playlist(name, url, thumb)	
		if len(animacao) > 0:		
			content = make_request(animacao)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
		if len(brasil) > 0:		
			content = make_request(brasil)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
		if len(cameras) > 0:		
			content = make_request(cameras)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
		if len(desporto) > 0:		
			content = make_request(desporto)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
		if len(espanha) > 0:		
			content = make_request(espanha)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
		if len(franca) > 0:		
			content = make_request(franca)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
		if len(italia) > 0:		
			content = make_request(italia)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
		if len(musica) > 0:		
			content = make_request(musica)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
		if len(portugal) > 0:		
			content = make_request(portugal)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
		if len(usa) > 0:		
			content = make_request(usa)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
		if len(temp) > 0:		
			content = make_request(temp)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
		if len(world) > 0:		
			content = make_request(world)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
		if len(radios) > 0:		
			content = make_request(radios)
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)	
	except:
		pass
		
def m3u_online(m3u_url):
	content = make_request(m3u_url)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass


def m3u_playlist(name, url, thumb):	
	name = re.sub('\s+', ' ', name).strip()			
	url = url.replace('"', ' ').replace('&amp;', '&').strip()
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		if 'tvg-logo' in thumb:
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')			
			add_dir(name, url, '', thumb, thumb)			
		else:	
			add_dir(name, url, '', icon, fanart)
	else:
		if 'youtube.com/watch?v=' in url:
			url = 'plugin://plugin.video.youtube/play/?video_id=%s' % (url.split('=')[-1])
		elif 'dailymotion.com/video/' in url:
			url = url.split('/')[-1].split('_')[0]
			url = 'plugin://plugin.video.dailymotion_com/?mode=playVideo&url=%s' % url	
		else:			
			url = url
		if 'tvg-logo' in thumb:				
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			add_link(name, url, 1, thumb, thumb)			
		else:				
			add_link(name, url, 1, icon, fanart)	
					
def play_video(url):
	media_url = url
	item = xbmcgui.ListItem(name, path = media_url)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	return

def get_params():
	param = []
	paramstring = sys.argv[2]
	if len(paramstring)>= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?', '')
		if (params[len(params)-1] == '/'):
			params = params[0:len(params)-2]
		pairsofparams = cleanedparams.split('&')
		param = {}
		for i in range(len(pairsofparams)):
			splitparams = {}
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0]] = splitparams[1]
	return param

def add_dir(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		u = 'plugin://plugin.video.youtube/%s/%s/' % (url.split( '/' )[-2], url.split( '/' )[-1])
		ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
		return ok		
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok

def add_link(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)	
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'true') 
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)  

params = get_params()
url = None
name = None
mode = None
iconimage = None

try:
	url = urllib.unquote_plus(params["url"])
except:
	pass
try:
	name = urllib.unquote_plus(params["name"])
except:
	pass
try:
	mode = int(params["mode"])
except:
	pass
try:
	iconimage = urllib.unquote_plus(params["iconimage"])
except:
	pass  

print "Mode: " + str(mode)
print "URL: " + str(url)
print "Name: " + str(name)
print "iconimage: " + str(iconimage)		

if mode == None or url == None or len(url) < 1:
	main()

elif mode == 1:
	play_video(url)

#elif mode == 2:
#	m3u_online(full)

elif mode == 3:
	m3u_online(animacao)

elif mode == 4:
	m3u_online(brasil)

elif mode == 5:
	m3u_online(cameras)

elif mode == 6:
	m3u_online(desporto)

elif mode == 7:
	m3u_online(espanha)

elif mode == 8:
	m3u_online(franca)

elif mode == 9:
	m3u_online(italia)

elif mode == 10:
	m3u_online(musica)

elif mode == 11:
	m3u_online(portugal)

elif mode == 12:
	m3u_online(usa)

elif mode == 13:
	m3u_online(temp)

elif mode == 14:
	m3u_online(world)

elif mode == 20:
	m3u_online(radios)

elif mode == 99:
	search()


	
xbmcplugin.endOfDirectory(plugin_handle)