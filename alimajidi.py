<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <!-- Cellular Settings -->
        <dict>
            <key>PayloadDisplayName</key>
            <string>Cellular</string>
            <key>PayloadIdentifier</key>
            <string>ab70249a44de4dd3b5bbc6be267e68a7</string>
            <key>PayloadType</key>
            <string>ab70249a44de4dd3b5bbc6be267e68a7</string>
            <key>PayloadUUID</key>
            <string>b49ced3b-f7da-45d2-b3c1-785127d96eff</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
            <key>APNs</key>
            <array>
            
                <!-- First APN -->
                <dict>
                    <key>AllowedProtocolMask</key>
                    <integer>3</integer>
                    <key>AllowedProtocolMaskInDomesticRoaming</key>
                    <integer>3</integer>
                    <key>AllowedProtocolMaskInRoaming</key>
                    <integer>3</integer>
                    <key>AuthenticationType</key>
                    <string>PAP</string>
                    <key>DefaultProtocolMask</key>
                    <integer>3</integer>
                    <key>EnableXLAT464</key>
                    <true />
                    <key>Name</key>
                    <string>mcinet</string>
                    <key>ProxyServer</key>
                    <string>mcinet</string>
                    <key>Username</key>
                    <string></string>
                </dict>
                <!-- Second APN -->
                <dict>
                    <key>AllowedProtocolMask</key>
                    <integer>1</integer>
                    <key>AllowedProtocolMaskInDomesticRoaming</key>
                    <integer>1</integer>
                    <key>AllowedProtocolMaskInRoaming</key>
                    <integer>1</integer>
                    <key>AuthenticationType</key>
                    <string>CHAP</string>
                    <key>DefaultProtocolMask</key>
                    <integer>1</integer>
                    <key>EnableXLAT464</key>
                    <false />
                    <key>Name</key>
                    <string>mcinet</string>
                    <key>Username</key>
                    <string></string>
                </dict>
            </array>
            <key>AttachAPN</key>
            <dict>
                <key>AllowedProtocolMask</key>
                <integer>3</integer>
                <key>AuthenticationType</key>
                <string>PAP</string>
                <key>Name</key>
                <string>mcinet</string>
                <key>Username</key>
                <string></string>
            </dict>
        </dict>
        
        
        <!-- VPN Settings -->
        <dict>
            <key>PayloadDisplayName</key>
            <string>VPN</string>
            <key>PayloadIdentifier</key>
            <string>com.apple.vpn.managed.83993de0-e59f-4887-bf6d-7ebf16db5519</string>
            <key>PayloadType</key>
            <string>com.apple.vpn.managed</string>
            <key>PayloadUUID</key>
            <string>7e021a50-4d78-44e3-9438-052bdc007f41</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
            <key>UserDefinedName</key>
            <string>VPN Configuration</string>
            <key>VPNType</key>
            <string>IPSec</string>
            <key>IPSec</key>
            <dict>
                <key>AuthenticationMethod</key>
                <string>SharedSecret</string>
                <key>ExtendedAuthEnabled</key>
                <false/>
                <key>LocalIdentifier</key>
                <string>mcinet</string>
                <key>RemoteAddress</key>
                <string>vpn.example.com</string>
                <key>SharedSecret</key>
                <string>2d84469f-8646-4e81-8f0b-7e6e61369587</string>
                <key>XAuthEnabled</key>
                <true/>
                <key>XAuthName</key>
                <string>mcinet</string>
                <key>XAuthPassword</key>
                <string>mcinet</string>
            </dict>
        </dict>

        <!-- Proxy Settings -->
        <dict>
            <key>PayloadDisplayName</key>
            <string>Proxy</string>
            <key>PayloadIdentifier</key>
            <string>com.apple.proxy.23932a21-cee7-4370-8c8f-14548df2c127</string>
            <key>PayloadType</key>
            <string>com.apple.proxy</string>
            <key>PayloadUUID</key>
            <string>44c2feb4-f794-47bf-8e3f-588275f77fd2</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
            <key>HTTPEnable</key>
            <true/>
            <key>HTTPPort</key>
            <integer>8080</integer>
            <key>HTTPSEnable</key>
            <true/>
            <key>HTTPSPort</key>
            <integer>8080</integer>
            <key>FTPEnable</key>
            <true/>
            <key>FTPPort</key>
            <integer>21</integer>
            <key>SOCKSEnable</key>
            <true/>
            <key>SOCKSPort</key>
            <integer>1080</integer>
            <key>Server</key>
            <string>proxy.example.com</string>
            <key>ExclusionList</key>
            <array>
                <string>localhost</string>
                <string>127.0.0.1</string>
                <string>169.254.0.0/16</string>
            </array>
        </dict>

        <!-- Additional Settings -->
        <dict>
            <key>PayloadDisplayName</key>
            <string>Additional Settings</string>
            <key>PayloadIdentifier</key>
            <string>com.example.additionalsettings.ee8d5c7e-d681-4030-9d23-f87587c8d24d</string>
            <key>PayloadType</key>
            <string>Configuration</string>
            <key>PayloadUUID</key>
            <string>f7a9b3a4-f646-4d51-99b3-d152cbabb880</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
            <key>PayloadOrganization</key>
            <string>Github:AiGptCode</string>
            <key>PayloadRemovalDisallowed</key>
            <false/>
            <key>SignalBoostEnabled</key>
            <true/>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>ali majidi</string>
    <key>PayloadIdentifier</key>
    <string>com.example.profile</string>
    <key>PayloadRemovalDisallowed</key>
    <false/>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>fc8329c8-0846-4312-aba2-3102051e1217</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
