Summary:	Mandriva graphical boot theme
Name:		mandriva-gfxboot-theme
Version:	4.1.19.26
Release:	3
License:	GPLv2+
Group:		System/Configuration/Boot and Init
URL:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/theme/mandriva-gfxboot-theme/trunk/
Source0:	%{name}-%{version}.tar.xz
Source1:	back.jpg
Source2:	welcome.jpg
Source3:	timer_a.jpg
Source4:	mandriva.pcx
Source5:	grub-gfxmenu
BuildRequires:	gfxboot-devel
Requires(post):	perl-Archive-Cpio
BuildArch:	noarch

%description
This package provides the Mandriva gfxboot theme. This theme is used by the
Mandriva installation to initialized the CDROM boot, and by installed system
to boot.

%prep
%setup -q

# our jpegs:
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} data-install/
cp %{SOURCE1} %{SOURCE3} data-boot/

%build
#gfxboot binary is needed for the build and is in /usr/sbin
#make sure we only build one task at a time since po generation is broken
#otherwise
PATH="$PATH:/usr/sbin" make

%install
install -d %{buildroot}%{_datadir}/gfxboot/themes/Mandriva/install/
install -m644 bootlogo bootlogo.dir/* %{buildroot}%{_datadir}/gfxboot/themes/Mandriva/install/
install -m644 message -D %{buildroot}%{_datadir}/gfxboot/themes/Mandriva/boot/message

install -m755 %{SOURCE5} -D %{buildroot}%{_sbindir}/grub-gfxmenu

%post
if [ "$1" -gt 1 ]; then
   %{_sbindir}/grub-gfxmenu --update-gfxmenu
fi

%files
%{_sbindir}/*
%{_datadir}/gfxboot/themes/Mandriva/
