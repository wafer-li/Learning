# Genymotion Problems & Solutions

Tags: Android

---

## 0. Intro

> This is an Problems & Solution Set of the Genymotion Android Emulator.
Although it's famous, since it using the VirtualBox to implement the x86 Emulator.
It becomes annoying, on Windows.

> So, that is some known problems and their solutions

## 1. Unable connect to virtual_device

> When this error occurs, genymotion will ask you to start the virtual device on VirtualBox, plase follow the instruction, and then you will get a ERROR message. 

There are several situations:

### 1) Virtual Host Error

> If you receive the ERROR message that is about the Virtual Host, it will appear to like this:
    
    Failed to open/create the internal network 'HostInterfaceNetworking-VirtualBox Host-Only Ethernet Adapter' (VERR_INTNET_FLT_IF_NOT_FOUND).
    Failed to attach the network LUN (VERR_INTNET_FLT_IF_NOT_FOUND).
    
#### Solution:
The solution is simple, accoring to the [stackoverflow](http://stackoverflow.com/questions/33725779/failed-to-open-create-the-internal-network-vagrant-on-windows10) :

> 
1. Open Windows Network Connections
2. Right click on VirtualBox Host only adapter that created
3. Choose properties
4. Check "VirtualBox NDIS6 Bridged Networking driver"
5. Disable and Enable the adapter

![Solution for Virtual Host Error](http://i.stack.imgur.com/Tkkws.png)

### 2) Virtual Device cannot link to network

> A bit confused, Why my Emulator cannot link to the internet?

#### Solution:

No a big deal, just open the wifi tab, and **link to the wifi**, it solved.
> It will **NOT** link to the real wifi, just the virtual network

