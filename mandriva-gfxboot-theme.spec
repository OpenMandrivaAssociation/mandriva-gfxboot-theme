
%define version 0.30
%define release %mkrel 1

Summary: Mandriva graphical boot theme
Name: mandriva-gfxboot-theme
Version: %version
Release: %release
License: GPL 
Group: System/Configuration/Boot and Init
URL: http://svn.mandriva.com/cgi-bin/viewvc.cgi/theme/gfxboot/trunk/
Source0: %{name}.tar
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gfxboot
Requires(post): perl-Archive-Cpio
Exclusivearch: %ix86 x86_64

%description
This package provides the Mandriva gfxboot theme. This theme is used by the
Mandriva installation to initialized the CDROM boot, and by installed system
to boot.

%prep
%setup -q

%build

make prefix=$RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

make install prefix=$RPM_BUILD_ROOT

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



