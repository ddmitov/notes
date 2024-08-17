;
; Simple Browser based on Mozilla and Internet Explorer ActiveX Components.
; Public domain.
; ddmitov@yahoo.com
;

#NoTrayIcon

#include <GUIConstants.au3>
#include <IE.au3>

If @OSType = "WIN32_NT" Then
   MsgBox (0+64, "Simple Browser", "Windows NT/2000/XP/Vista detected! Please use Simple Browser for NT based systems!")
   Exit
EndIf

; Read browser-9x.ini.
$engine = IniRead ("browser-9x.ini", "Simple_Browser", "engine", "mozilla")
$name = IniRead ("browser-9x.ini", "Simple_Browser", "name", "Simple Browser")
$host = IniRead ("browser-9x.ini", "Simple_Browser", "host", "localhost")
$port = IniRead ("browser-9x.ini", "Simple_Browser", "port", "80")
$index = IniRead ("browser-9x.ini", "Simple_Browser", "index", "index.htm")

$protocol = "http"
$semicolon = ":"
$slash = "/"

$address = $protocol&$semicolon&$slash&$slash&$host&$semicolon&$port&$slash&$index

_IEErrorHandlerRegister ()

If $engine = "choose" Then
   $answer = MsgBox (4+32+256, "Simple Browser", "Do you want to use Internet Explorer rendering engine? " & "Gecko rendering engine is the default one.")
   If $answer = 7 Then
      ; Register Mozilla ActiveX.
      RunWait('Regsvr32 /s "'&@ScriptDir&'\mozilla\mozctlx.dll"')
      $oIE = ObjCreate("Mozilla.Browser.1")
   Else
      $oIE = _IECreateEmbedded ()
   EndIf
EndIf

If $engine = "gecko" Then
   RunWait('Regsvr32 /s "'&@ScriptDir&'\mozilla\mozctlx.dll"')
   $oIE = ObjCreate("Mozilla.Browser.1")
EndIf

If $engine = "ie" Then
   $oIE = _IECreateEmbedded ()
EndIf

; Calculate visible screen dimensions.
$one_percent_width = @DesktopWidth / 100
$one_percent_height = @DesktopHeight / 100
$width = $one_percent_width * 98
$height = $one_percent_height * 91

GUICreate($name, @DesktopWidth, @DesktopHeight, 1, 1, $WS_MAXIMIZE + $WS_OVERLAPPEDWINDOW + $WS_VISIBLE)
$GUIActiveX = GUICtrlCreateObj($oIE, 10, 10, $width, $height)

; Show GUI.
GUISetState(@SW_MAXIMIZE)
_IENavigate ($oIE, $address)

; Waiting for user to close the window.
While 1
      $msg = GUIGetMsg()
      Select
            Case $msg = $GUI_EVENT_CLOSE
                  ExitLoop
      EndSelect
WEnd

; Unregister the Mozilla ActiveX.
If $engine = "gecko" Then
   RunWait('Regsvr32 -u /s "'&@ScriptDir&'\mozilla\mozctlx.dll"')
EndIf

GUIDelete()

Exit
