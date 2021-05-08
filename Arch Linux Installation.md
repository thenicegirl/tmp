# Arch Linux Installation

> First of all `ArchLinux` is really not suitable for your own working development machine, if your code is incredibly precious, please don't use `Arch`. whether you agree with it or not, this is a word of advice.

The best and most complete tutorial for installing Arch is the official [Installation guide](https://wiki.archlinux.org/index.php/installation_guide) and the [Wiki](https://wiki.archlinux.org/), although some of the content has a *other language* version, but the *other language* translation sometimes lags behind the English version, it is not recommended to rely on the *other language* Wiki. and the official Wiki is written in a more documentation-oriented way, without the step-by-step installation process that we are used to, causing reading and use difficulties for students who are not familiar with this writing style. The tutorials that can be found in *other tutorial* are often older, or do not mention or ignore some of the mistakes that novices tend to make.

## 1. Make sure again that the system is in **UEFI** mode

After a series of message swipes, you can see that you have logged in as root to install the system, and the first command to execute at this point is

```bash
ls /sys/firmware/efi/efivars
```

If it outputs a bunch of stuff, i.e. efi variables, then you are in UEFI mode. Otherwise, please make sure your boot method is UEFI.

## 2. Connecting to the network
### Connect wirelessly:

Wireless connections are made using iwctl:

```bash
iwctl #Enter the interactive command line
device list #List the device names, e.g. wireless NIC is called wlan0
station wlan0 scan # scan for networks
station wlan0 get-networks # list networks For example, if you want to connect to the CMCC-5AQ7 wireless
station wlan0 connect CMCC-5AQ7 #to connect enter the password
exit #exit after success
```

### Wired connection:
Normally, just plug in a network cable (DHCP) that has been split from a router that is already connected to the network, and you will be able to connect directly.

You can wait for a few seconds for the network to establish a link before you proceed to the next step of testing the network

## 3. Test network
```bash
ping www.gnu.org
```
Wait a moment, if you can see the data return, that means you are connected, `ctrl+c` to terminate the current command. If you still cannot connect, use the `ip link set xxx up` command to confirm that you have activated the corresponding network card, and then continue the network link and test again. If you see an error like `Operation not possible due to RF-kill`, continue to try `rfkill unblock wifi` to unlock the wireless card.
try systemctl start dhcpcd that test again

## 4. disable reflector (**Optional**)
The new 2020 version of `archliveiso` adds the `reflector` service, which updates the `mirrorlist` by itself and in certain cases can accidentally delete some useful source information. The first thing you should do here is to disable it after networking. It may be a good tool to use, but obviously it is not suitable to be enabled during installation, especially in some where like China.
```bash
systemctl stop reflector.service
```

## 5. update the system clock
```bash
timedatectl set-ntp true #Synchronize the system time with the network time
timedatectl status #Check the service status
```

## 6. change the domestic mirror source to speed up the download speed (**Optional if you use a VPN**)

```bash
vim /etc/pacman.d/mirrorlist #If you don't know how to vim, pay attention to the vim steps in the video here
```

Put the top is the update source that will be used, put CSU ustc's or Tsinghua's at the top

7. Partitioning
A total of three partitions are set up here, which will satisfy most people's needs. This step will erase the entire contents of the disk, so please check beforehand.

* EFI partition: /efi 800M
* Root directory: /100G
* User home directory: /home All remaining, the larger the better.
> The size of the root directory here is just for reference, generally speaking, 100G is enough for daily use of linux. The minimum recommended size of the root directory is not less than 50G. A small root directory will cause problems such as not being able to update system packages.

First convert the disk to `gpt` type

```bash
lsblk #Show partition status
parted /dev/sdx #execute parted to change the disk type
(parted)mktable #Type mktable
New disk label type? gpt #type gpt to change the disk type to gpt, if the disk has data it will warn you, type yes
quit #Finally quit the parted command line interaction
```

Next, use the cfdisk command to partition the disk

```bash
cfdisk /dev/sdx # to perform a partitioning operation, assigning the size and type of each partition
fdisk -l #Review the disk
```

The detailed operation of `cfdisk` partitioning is described in the video. It is generally recommended to set the `EFI` partition as the first partition of the disk, it is said that some motherboards may have incompatibility problems if you do not set `EFI` as the first partition.

## 8. formatting
The `sdax` here is just an example, depending on your actual situation, please pay attention to the actions in the video.

```bash
#if the disk has data, it will ask 'proceed any way?' y enter, that's it
mkfs.ext4 /dev/sdax #Format the two partitions in the root and home directories
mkfs.vfat /dev/sdax #Format the efi partition
mkswap -f /dev/sdax
swapon /dev/sdax
```

## 9. Mount
When mounting, the mounts are sequential and need to start from the root directory
Here `sdax` is just an example, it depends on your situation, please pay attention to the video.
```bash
mount /dev/sdax /mnt
mkdir /mnt/home
mount /dev/sdax /mnt/home
mkdir /mnt/efi
mount /dev/sdax /mnt/efi
mkdir /mnt/boot/efi
mount /dev/sdax /mnt/boot/efi
```

## 10. Install the system

Base package
```bash
pacstrap /mnt base-devel linux linux-firmware #base-devel is required for the installation of the AUR package
```

Functional software
```bash
pacstrap /mnt dhcpcd iwd vim sudo bash-completion #one required for wired, one required for wireless, one editor, one power-up tool, one complementary tool, and dhcpcd for iwd.
```

# 11. Generate fstab files

`fstab` is used to define disk partitions
```bash
genfstab -U /mnt >> /mnt/etc/fstab
```
Review `/mnt/etc/fstab` to make sure there are no errors
```bash
cat /mnt/etc/fstab
```

## 12. change root

Switch the environment to the new system under `/mnt`
```bash
arch-chroot /mnt
```

## 13. Set the hostname and time zone

First set the hostname in `/etc/hostname`
```bash
vim /etc/hostname
```
Add the hostname you want for the host, for example `myarch`.

Next, set the entries in /etc/hosts to match it.
```bash
vim /etc/hosts
```

Add the following
```bash
127.0.0.1   localhost
::1         localhost
127.0.1.1   myarch.localdomain    myarch
```

> In some cases, if you do not set the hostname, you may not be able to start the GUI application under KDE when the network conditions change, and you may get an error in the terminal like `No protocol specified qt.qpa.xcb: could not connect to display`. This situation is extremely rare, and the group owner has only encountered feedback from one user. Related reference links:

Then set the timezone and create a symbolic connection under `/etc/localtime` with the appropriate timezone in `/usr`.
```bash
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

## 14. Hardware time setting

Synchronize the system time to the hardware time
```bash
hwclock --systohc
```

## 15. Setting Locale
`Locale` determines the language, writing conventions and character set used by the software.

Edit `/etc/locale.gen` and remove the `en_US.UTF-8` line and the comment symbol (#) for `en_CN.UTF-8`.

Then use the following command to generate the locale.
```bash
locale-gen
```
Enter the following into `/etc/locale.conf`
```bash
echo 'LANG=en_US.UTF-8' > /etc/locale.conf
```

## 16. Set the password for the root user
```bash
passwd root
```

## 17. Install microcode
```bash
pacman -S intel-ucode #Intel
pacman -S amd-ucode #AMD
```

## 18. Installing the bootloader
```bash
pacman -S grub efibootmgr #grub is the bootloader, efibootmgr is used by the grub script to write boot items to NVRAM.
grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=GRUB #Take the name GRUB and install grubx64.efi to the previously specified location
```
Next, edit the `/etc/default/grub` file, remove the `quiet` parameter from the last line of `GRUB_CMDLINE_LINUX_DEFAULT`, and change the log level from 3 to 5. This is to make it easier to troubleshoot system errors if they occur. Also add the `nowatchdog` parameter, which can significantly improve the switching speed. If you don't know how to use vim, pay attention to the video.
```bash
//////////////
vim /etc/default/grub
```

Finally, generate the configuration files needed for GRUB

```bash
grub-mkconfig -o /boot/grub/grub.cfg
```
> After installation on some motherboards, you may find that there is no boot entry. This is because the `UEFI` firmware on some motherboards requires bootable files to be stored in a specific location before displaying the `UEFI NVRAM` boot entry, and does not support custom storage of efi files (e.g. MSI Z170-A Gaming PRO). The solution is to install GRUB under the default boot path. reinsert the installation flash drive, mount the directory, chroot to `/mnt`, and then you can directly move the already generated efi files to the default directory as shown in the code below. You only need to try the following command if your motherboard does not show the boot entry after the installation is completed, no need to execute it for normal installation. Official reference documentation
```bash
/////////
mkdir -p /efi/EFI/BOOT
mv /efi/EFI/GRUB/grubx64.efi /efi/EFI/BOOT/BOOTX64.EFI
```

## 19. Finish the installation
```bash
exit # Return to the installation environment #
umount -R /mnt # Uninstall the new partition
reboot # reboot
```

Note that you have to unplug your flash drive before rebooting, otherwise you will still be in the installer instead of the installed system after rebooting. After reboot, turn on the dhcp service to connect to the network
```bash
systemctl start dhcpcd #Start dhcp immediately
ping www.baidu.com #Test the network connection
```

If it is a wireless link, you also need to start `iwd` to connect to the network using `iwctl`
```bash
systemctl start iwd #Start iwd immediately
iwctl # Connect to the wireless network in the same way as before
```
At this point, a basic, UI-less installation of Arch Linux has been completed. Immediately following the next section, let's install the graphical interface.

> In April 2021, archlinux included an install script in the install image, which is a one-click install script that provides a few options for a quick installation. It is similar to all one-click install scripts in that it provides an automated, inflexible installation process. The drawbacks are: limited file system formats, limited to one disk, no source specification, limited desktop options, no manual intervention for automatic partitioning, direct crash exit for input errors, UEFI support only, etc. It is **not recommended** to use such installation scripts, and besides all the above reasons, beginners will not learn anything from such installation process. If you need to quickly boot a basic archlinux environment for any reason, then try this script.

## some other...
```
//////////
lspci | grep VGA
pacman -S xf86-video-vesa
pacman -S xorg
pacman -S ttf-dejavu wqy-microhei
pacman -S plasma kde-applications
systemctl enable sddm
systemctl enable NetworkManager

reboot

fcitx-im fcitx-config fcitx-googlepinyin
```

systemctl enable dhcpcd

systemctl start dhcpcd
