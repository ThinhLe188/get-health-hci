tcl86t.dll      tk86t.dll       _tk_data             �    �  z   Htk86t.dll api-ms-win-crt-string-l1-1-0.dll api-ms-win-crt-convert-l1-1-0.dll api-ms-win-core-errorhandling-l1-1-0.dll api-ms-win-core-file-l2-1-0.dll api-ms-win-core-file-l1-1-0.dll api-ms-win-core-debug-l1-1-0.dll api-ms-win-crt-environment-l1-1-0.dll tcl86t.dll _tk_data\text.tcl api-ms-win-core-heap-l1-1-0.dll ucrtbase.dll api-ms-win-core-synch-l1-1-0.dll api-ms-win-core-processthreads-l1-1-0.dll api-ms-win-core-localization-l1-2-0.dll api-ms-win-core-libraryloader-l1-1-0.dll api-ms-win-core-string-l1-1-0.dll api-ms-win-core-util-l1-1-0.dll api-ms-win-core-file-l1-2-0.dll _tk_data\ttk\utils.tcl api-ms-win-crt-heap-l1-1-0.dll api-ms-win-crt-utility-l1-1-0.dll VCRUNTIME140.dll api-ms-win-core-sysinfo-l1-1-0.dll api-ms-win-core-interlocked-l1-1-0.dll api-ms-win-core-timezone-l1-1-0.dll api-ms-win-core-synch-l1-2-0.dll _tk_data\tk.tcl _tk_data\license.terms api-ms-win-core-datetime-l1-1-0.dll api-ms-win-crt-time-l1-1-0.dll api-ms-win-core-rtlsupport-l1-1-0.dll api-ms-win-core-processthreads-l1-1-1.dll api-ms-win-core-console-l1-1-0.dll _tk_data\ttk\ttk.tcl api-ms-win-core-handle-l1-1-0.dll _tk_data\ttk\fonts.tcl api-ms-win-core-memory-l1-1-0.dll _tk_data\ttk\cursors.tcl api-ms-win-core-profile-l1-1-0.dll api-ms-win-core-namedpipe-l1-1-0.dll api-ms-win-crt-math-l1-1-0.dll api-ms-win-crt-runtime-l1-1-0.dll api-ms-win-crt-stdio-l1-1-0.dll api-ms-win-core-processenvironment-l1-1-0.dll proc _ipc_server {channel clientaddr clientport} {
set client_name [format <%s:%d> $clientaddr $clientport]
chan configure $channel \
-buffering none \
-encoding utf-8 \
-eofchar \x04 \
-translation cr
chan event $channel readable [list _ipc_caller $channel $client_name]
}
proc _ipc_caller {channel client_name} {
chan gets $channel cmd
if {[chan eof $channel]} {
chan close $channel
exit
} elseif {![chan blocked $channel]} {
if {[string match "update_text*" $cmd]} {
global status_text
set first [expr {[string first "(" $cmd] + 1}]
set last [expr {[string last ")" $cmd] - 1}]
set status_text [string range $cmd $first $last]
}
}
}
set server_socket [socket -server _ipc_server -myaddr localhost 0]
set server_port [fconfigure $server_socket -sockname]
set env(_PYI_SPLASH_IPC) [lindex $server_port 2]
image create photo splash_image
splash_image put $_image_data
unset _image_data
proc canvas_text_update {canvas tag _var - -} {
upvar $_var var
$canvas itemconfigure $tag -text $var
}
package require Tk
set image_width [image width splash_image]
set image_height [image height splash_image]
set display_width [winfo screenwidth .]
set display_height [winfo screenheight .]
set x_position [expr {int(0.5*($display_width - $image_width))}]
set y_position [expr {int(0.5*($display_height - $image_height))}]
frame .root
canvas .root.canvas \
-width $image_width \
-height $image_height \
-borderwidth 0 \
-highlightthickness 0
.root.canvas create image \
[expr {$image_width / 2}] \
[expr {$image_height / 2}] \
-image splash_image
wm attributes . -transparentcolor magenta
.root.canvas configure -background magenta
pack .root
grid .root.canvas -column 0 -row 0 -columnspan 1 -rowspan 2
wm overrideredirect . 1
wm geometry . +${x_position}+${y_position}
wm attributes . -topmost 1
raise .�PNG

   IHDR  �  �   ����   	pHYs    g��R  �IDATx���]�e�a��g���9s�|gƓ1N�$N���i���IZpU��"qQ��@B��H��zGsC/ � 	�*U �^PD�I�c5M����N<cO�����{/.�$3�'�gR�z��O��Yg�}�u��׻�{��y�c ���  �	���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T.�KO_��/|�Ŝݚ��C����= h��[�ww��z>����������,��ŭy�\��3�����rqk��r��<�G���l2�1�z	܅�r̯�Z��ȓI>���|��ɟ;�������o�=}-_xv3�{v3���Y�If�d�w?r2�w=�A��V�w�����;�$�1�L��?�_��{����g�xf3������l��^�!�|���$c>�c������ ��p�]��o]��tH���ۋ\Y�泿{!�d6ɇN�r�u��n��o�����N&�rL�cΆ,�1[�1Y��'��'?|�u>"�aq܅�~q��%�[6�,r1�?������K���O]�_�O痿v5��${��e�ut%�V'�]��t�CØO�t&.�w%\p��ϗy��<�W�p{�3�1���9�\���'.�S�r&O]^$;�dL&��;62�$�6����C~懎��o��E�V!\p���>������R/����ۋ��'/��������s�>O��H�!��?x8{�1O]���0d}9���D�;t~{�����=�&�-�dw������^{��`%�t����`V�C�8�s�;V&y�#���k��@'�;t~{�am��!�CN'7Vް3_���\�'=���190��'V��S���O^�ܘd2]���?x�:$�"\p�^�Y���+�1�g���\Ivy|s�'���减gu\�g>�������ps�5r��i~�ｌ�g9<ܡ���ՄCfI6f�dw��U�c2.���O_�g<�������o�����e�I2��{������;(f�wh��dH�a����+&\����Řg�ȇޱ�_�꥗E+�8�c~mo"�wh���f2rders�ˌ�����<���YƗ8�L�{,ʀWK���O_:�Z���N2]�����"�����!��(��r��&�3�m��W^��Û�p�:�vK��ds1f�!��%�ۄkL��I�ϕ�|�݇nn�d��c���w��ӌ;�d2$�qu���̻��o���2_|q+��m-����7�+��y]����}�+91�s�o\�y��n�}h5�����4�1x}���1[���d��=r2�V�&�;!\�*\_����;��f6�λ�%���/�����Z����K�a}�r�ru���e�{r5Y��O_�_��c��q���p����X�W/�7.>�'v����N�ͯ�#'�o<c07�aM�k����3����L�ol���Y���|�/��a�wL��x~{3�q�L�\~+��<�[�l_����V>|j5+�˛���1_���?}�@Η7gc�����Z�g?z*y��+��h����W/淮���t/;���n/2����2�;9��ȏ�:�|���|�gw��2��S��mfR�1g����8�����.x��]���l��q2f����HVקY[�f\��L&ٜo�g�?���bv5&�tȯ������P�n7�Z���7��6�1��.��7�_�W���$Y�Y90�0&Gǵܛ�y��=������l#>���_�R|�qg��_��d�ӧ7���V���QwO���K��y���YY�d�3'99��{ˑ�Z�sng3_��b�<��\y>�z���'Y��/�80�|�J~��G��7���Pc�ɐ�w �$Y����K�2ݘeok�CY͉��^,rf�J�޾�f��<���t��,rf������
�dȸ�������嘿z����}ۍ��ѥB�~$yz�r���fws���,�q��w��jv��e�嘭���\_dog���2�1�ҕ�S���gO̰6K�c�������䯼�h�1��I�����S�����"�yq��ċ1�{�I��w�Y.ƌ�+?����b5y��7�<��8���ϒ�e~��f�ݜ������Ð���$kg��E�x�{n�jvg���,2�$ӕI�ɐ��$��If+�LgC&�!�ɍ�!�ِ�|��mC��z1���=y��Z��I��Y���}+?u�������4�9�:�!S.��8�xK[f�ӛ��qd���i��d�3�Kf�!����<�8_~�mZ���a����Ե�<�~<�V��G<��v�F�5����ճ����ȑ�2ÁY�Y���힬�j�7z �F:�}=��;���Ε#9~�@6f+Y�L3���1��Yγ��gw��&p6Lsp��C��̆�!Z�����#'�󏟼����՟xg>����k�1+��	���"\�e�c����#�N������4YM�1�%w�ǟ<}0��Z���/旞��������������<qq;��X��:x��y擷��o~�${�E�&��n�~e/^�7������f%ɿ�����ë���7+�y˚$�y���}GV2�wn��8�K�1�K����^��oF���G��ȿ����M��\}���\*�7���2�a����p�,΀7�K��9{ �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� �"\ T. � U��*�@���pPE� ����hz�B K�   eXIfMM *          �S�    IEND�B`�