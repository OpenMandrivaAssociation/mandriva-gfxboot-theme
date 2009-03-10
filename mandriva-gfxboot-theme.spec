%define version 4.1.19.8
%define release %mkrel 1

Summary: Mandriva graphical boot theme
Name: mandriva-gfxboot-theme
Version: %version
Release: %release
License: GPL 
Group: System/Configuration/Boot and Init
URL: http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/theme/mandriva-gfxboot-theme/trunk/
Source: mandriva-gfxboot-theme-%{version}.tar.lzma
#
Source1: back.jpg
Source2: welcome.jpg
Source3: timer_a.jpg
#Source4: mandriva.pcx
Source5: grub-gfxmenu

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gfxboot-devel
Requires(post): perl-Archive-Cpio
Exclusivearch: %ix86 x86_64

%description
This package provides the Mandriva gfxboot theme. This theme is used by the
Mandriva installation to initialized the CDROM boot, and by installed system
to boot.

%prep
%setup -q

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



