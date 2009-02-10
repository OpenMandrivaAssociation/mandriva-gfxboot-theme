%define version 4.1.19
%define release %mkrel 1

Summary: Mandriva graphical boot theme
Name: mandriva-gfxboot-theme
Version: %version
Release: %release
License: GPL 
Group: System/Configuration/Boot and Init
URL: http://svn.mandriva.com/cgi-bin/viewvc.cgi/theme/gfxboot/trunk/
# comes from gfxboot-4.1.19-2.1.src.rpm:
Source0: openSUSE.tar.bz2
#
Source1: back.jpg
Source2: welcome.jpg
Source3: timer_a.jpg
#Source4: text.jpg
Source5: grub-gfxmenu

Patch0001: add-Norsk-nynorsk-in-language-menu-and-rename.patch
Patch0002: replace-openSUSE-strings-with-Mandriva-Linux.patch
Patch0003: enhance-po-Makefile.patch
Patch0004: we-use-i586-not-i386.patch
Patch0005: make-the-livecd-syslinux-more-alike-non-livecd-sys.patch
Patch0006: replace-SUSE-s-stage1-para-options-with-ours.patch
Patch0007: adapt-dud-to-mandriva-stage1-para-updatemodules.patch
Patch0008: more-serious-message-in-case-of-32bit-resp-64bit-i.patch
Patch0009: dynamic-renaming-of-bootloader-entries.patch
Patch0010: translate-mandriva-bootloader-entries.patch
Patch0011: adapt-to-mandriva-timer.patch
Patch0012: we-want-all-langs-by-default-in-our-boot-gfxmenu-f.patch
Patch0013: adapt-menu-boot-options-location-size-to-mandriva-ba.patch
Patch0014: one-line-panel-instead-of-two-lines.patch
Patch0015: we-do-not-handle-multiple-splash-files-splashy.patch
Patch0016: use-more-explicit-Kernel-Option-instead-of-Kernel.patch
Patch0017: only-show-the-Boot-Options-entry-when-Fkey-for-Ke.patch
Patch0018: do-not-show-keyboard-layout-choice.patch
Patch0019: do-not-display-some-menu-entries-eg-noacpi.patch
Patch0020: do-not-check-there-is-enough-memory.patch
Patch0021: do-not-have-files-both-in-the-tarball-and-in-the-dir.patch
Patch0022: we-want-support-for-all-languages-in-grub-s-gfxmenu.patch
Patch0023: get-rid-of-some-easter-eggs-esp.-penguins.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gfxboot-devel
Requires(post): perl-Archive-Cpio
Exclusivearch: %ix86 x86_64

%description
This package provides the Mandriva gfxboot theme. This theme is used by the
Mandriva installation to initialized the CDROM boot, and by installed system
to boot.

%prep
%setup -q -n themes/openSUSE

%if 0
git init ; git add . ; git commit -m "imported %SOURCE0" ; git tag vanilla
git am %patches
%else
for i in %patches; do patch -p1 -i $i; done
%endif

# goes with get-rid-of-some-easter-eggs-esp.-penguins.patch:
rm data-*/{hapysuse.mod,kroete.dat,pabout.txt,panim.jpg,panim_a.jpg,pback.jpg,phead.jpg,text.jpg}
rm -r penguin_src src/penguin.inc

# english talk file is big and unused by default, get rid of it:
rm data-install/en.tlk

# our jpegs:
install -m 644 %{SOURCE1} %{SOURCE2} %{SOURCE3} data-install/
install -m 644 %{SOURCE1} %{SOURCE3} data-boot/

%build
#gfxboot binary is needed for the build and is in /usr/sbin
PATH="$PATH:/usr/sbin" %make

%install
rm -rf $RPM_BUILD_ROOT
dest=%{buildroot}%{_datadir}/gfxboot/themes/Mandriva
install -d $dest/install $dest/boot
install bootlogo bootlogo.dir/* $dest/install/
install message $dest/boot/

# install grub-gfxmenu
install -d %{buildroot}%{_sbindir}
install %{SOURCE5} %{buildroot}%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" -gt 1 ]; then
   %_sbindir/grub-gfxmenu --update-gfxmenu
fi

%files
%defattr(-,root,root,-)
%doc
%_sbindir/*
%_datadir/gfxboot/themes/Mandriva/



