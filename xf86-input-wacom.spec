#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0DAD9D6C60D924AC (killertofu@gmail.com)
#
Name     : xf86-input-wacom
Version  : 0.36.0
Release  : 15
URL      : https://sourceforge.net/projects/linuxwacom/files/xf86-input-wacom/xf86-input-wacom-0.36.0.tar.bz2
Source0  : https://sourceforge.net/projects/linuxwacom/files/xf86-input-wacom/xf86-input-wacom-0.36.0.tar.bz2
Source99 : https://sourceforge.net/projects/linuxwacom/files/xf86-input-wacom/xf86-input-wacom-0.36.0.tar.bz2.sig
Summary  : X.Org Wacom Tablet driver.
Group    : Development/Tools
License  : GPL-2.0
Requires: xf86-input-wacom-bin
Requires: xf86-input-wacom-lib
Requires: xf86-input-wacom-data
Requires: xf86-input-wacom-man
BuildRequires : doxygen
BuildRequires : graphviz
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xrandr)

%description
This package provides the X.Org X11 driver for Wacom and Wacom-like tablets.
It obsoletes the linuxwacom driver and supports X server versions 1.7 and
higher. Server versions lower than 1.7 may be supported by this driver, but
users are encouraged to use the old linuxwacom driver instead.

%package bin
Summary: bin components for the xf86-input-wacom package.
Group: Binaries
Requires: xf86-input-wacom-data = %{version}-%{release}
Requires: xf86-input-wacom-man = %{version}-%{release}

%description bin
bin components for the xf86-input-wacom package.


%package data
Summary: data components for the xf86-input-wacom package.
Group: Data

%description data
data components for the xf86-input-wacom package.


%package dev
Summary: dev components for the xf86-input-wacom package.
Group: Development
Requires: xf86-input-wacom-lib = %{version}-%{release}
Requires: xf86-input-wacom-bin = %{version}-%{release}
Requires: xf86-input-wacom-data = %{version}-%{release}
Provides: xf86-input-wacom-devel = %{version}-%{release}

%description dev
dev components for the xf86-input-wacom package.


%package lib
Summary: lib components for the xf86-input-wacom package.
Group: Libraries
Requires: xf86-input-wacom-data = %{version}-%{release}

%description lib
lib components for the xf86-input-wacom package.


%package man
Summary: man components for the xf86-input-wacom package.
Group: Default

%description man
man components for the xf86-input-wacom package.


%prep
%setup -q -n xf86-input-wacom-0.36.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538856094
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1538856094
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/systemd/system/wacom-inputattach@.service
/usr/lib64/udev/rules.d/wacom.rules

%files bin
%defattr(-,root,root,-)
/usr/bin/isdv4-serial-debugger
/usr/bin/isdv4-serial-inputattach
/usr/bin/xsetwacom

%files data
%defattr(-,root,root,-)
/usr/share/X11/xorg.conf.d/70-wacom.conf

%files dev
%defattr(-,root,root,-)
/usr/include/xorg/Xwacom.h
/usr/include/xorg/isdv4.h
/usr/include/xorg/wacom-properties.h
/usr/include/xorg/wacom-util.h
/usr/lib64/pkgconfig/xorg-wacom.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/input/wacom_drv.so

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xsetwacom.1
/usr/share/man/man4/wacom.4
