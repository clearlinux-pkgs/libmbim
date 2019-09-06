#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libmbim
Version  : 1.20.0
Release  : 8
URL      : https://www.freedesktop.org/software/libmbim/libmbim-1.20.0.tar.xz
Source0  : https://www.freedesktop.org/software/libmbim/libmbim-1.20.0.tar.xz
Summary  : MBIM modem protocol helper library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libmbim-bin = %{version}-%{release}
Requires: libmbim-data = %{version}-%{release}
Requires: libmbim-lib = %{version}-%{release}
Requires: libmbim-libexec = %{version}-%{release}
Requires: libmbim-license = %{version}-%{release}
Requires: libmbim-man = %{version}-%{release}
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gudev-1.0)

%description
libmbim is a glib-based library for talking to WWAN modems and devices which
speak the Mobile Broadband Interface Model (MBIM) protocol.

%package bin
Summary: bin components for the libmbim package.
Group: Binaries
Requires: libmbim-data = %{version}-%{release}
Requires: libmbim-libexec = %{version}-%{release}
Requires: libmbim-license = %{version}-%{release}

%description bin
bin components for the libmbim package.


%package data
Summary: data components for the libmbim package.
Group: Data

%description data
data components for the libmbim package.


%package dev
Summary: dev components for the libmbim package.
Group: Development
Requires: libmbim-lib = %{version}-%{release}
Requires: libmbim-bin = %{version}-%{release}
Requires: libmbim-data = %{version}-%{release}
Provides: libmbim-devel = %{version}-%{release}
Requires: libmbim = %{version}-%{release}
Requires: libmbim = %{version}-%{release}

%description dev
dev components for the libmbim package.


%package doc
Summary: doc components for the libmbim package.
Group: Documentation
Requires: libmbim-man = %{version}-%{release}

%description doc
doc components for the libmbim package.


%package lib
Summary: lib components for the libmbim package.
Group: Libraries
Requires: libmbim-data = %{version}-%{release}
Requires: libmbim-libexec = %{version}-%{release}
Requires: libmbim-license = %{version}-%{release}

%description lib
lib components for the libmbim package.


%package libexec
Summary: libexec components for the libmbim package.
Group: Default
Requires: libmbim-license = %{version}-%{release}

%description libexec
libexec components for the libmbim package.


%package license
Summary: license components for the libmbim package.
Group: Default

%description license
license components for the libmbim package.


%package man
Summary: man components for the libmbim package.
Group: Default

%description man
man components for the libmbim package.


%prep
%setup -q -n libmbim-1.20.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567782568
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1567782568
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libmbim
cp COPYING %{buildroot}/usr/share/package-licenses/libmbim/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/libmbim/COPYING.LIB
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mbim-network
/usr/bin/mbimcli

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/mbimcli

%files dev
%defattr(-,root,root,-)
/usr/include/libmbim-glib/libmbim-glib.h
/usr/include/libmbim-glib/mbim-atds.h
/usr/include/libmbim-glib/mbim-auth.h
/usr/include/libmbim-glib/mbim-basic-connect.h
/usr/include/libmbim-glib/mbim-cid.h
/usr/include/libmbim-glib/mbim-compat.h
/usr/include/libmbim-glib/mbim-device.h
/usr/include/libmbim-glib/mbim-dss.h
/usr/include/libmbim-glib/mbim-enum-types.h
/usr/include/libmbim-glib/mbim-enums.h
/usr/include/libmbim-glib/mbim-error-types.h
/usr/include/libmbim-glib/mbim-errors.h
/usr/include/libmbim-glib/mbim-intel-firmware-update.h
/usr/include/libmbim-glib/mbim-message.h
/usr/include/libmbim-glib/mbim-ms-basic-connect-extensions.h
/usr/include/libmbim-glib/mbim-ms-firmware-id.h
/usr/include/libmbim-glib/mbim-ms-host-shutdown.h
/usr/include/libmbim-glib/mbim-phonebook.h
/usr/include/libmbim-glib/mbim-proxy-control.h
/usr/include/libmbim-glib/mbim-proxy.h
/usr/include/libmbim-glib/mbim-qmi.h
/usr/include/libmbim-glib/mbim-sms.h
/usr/include/libmbim-glib/mbim-stk.h
/usr/include/libmbim-glib/mbim-ussd.h
/usr/include/libmbim-glib/mbim-utils.h
/usr/include/libmbim-glib/mbim-uuid.h
/usr/include/libmbim-glib/mbim-version.h
/usr/lib64/libmbim-glib.so
/usr/lib64/pkgconfig/mbim-glib.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libmbim-glib/MbimDevice.html
/usr/share/gtk-doc/html/libmbim-glib/MbimMessage.html
/usr/share/gtk-doc/html/libmbim-glib/MbimProxy.html
/usr/share/gtk-doc/html/libmbim-glib/annotation-glossary.html
/usr/share/gtk-doc/html/libmbim-glib/api-index-full.html
/usr/share/gtk-doc/html/libmbim-glib/ch01.html
/usr/share/gtk-doc/html/libmbim-glib/ch02.html
/usr/share/gtk-doc/html/libmbim-glib/ch03.html
/usr/share/gtk-doc/html/libmbim-glib/ch04.html
/usr/share/gtk-doc/html/libmbim-glib/ch05.html
/usr/share/gtk-doc/html/libmbim-glib/ch06.html
/usr/share/gtk-doc/html/libmbim-glib/ch07.html
/usr/share/gtk-doc/html/libmbim-glib/home.png
/usr/share/gtk-doc/html/libmbim-glib/index.html
/usr/share/gtk-doc/html/libmbim-glib/left-insensitive.png
/usr/share/gtk-doc/html/libmbim-glib/left.png
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-ATDS.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-Auth.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-Basic-Connect.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-Command-IDs.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-Common-utilities.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-DSS.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-Deprecated-API.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-Enumerations-and-Flags.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-Errors.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-Intel-Firmware-Update.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-MS-Firmware-ID.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-MS-Host-Shutdown.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-Ms-Basic-Connect-Extensions.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-Phonebook.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-QMI.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-SMS.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-STK.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-USSD.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-UUIDs.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-Version-checks.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib.devhelp2
/usr/share/gtk-doc/html/libmbim-glib/object-tree.html
/usr/share/gtk-doc/html/libmbim-glib/right-insensitive.png
/usr/share/gtk-doc/html/libmbim-glib/right.png
/usr/share/gtk-doc/html/libmbim-glib/style.css
/usr/share/gtk-doc/html/libmbim-glib/up-insensitive.png
/usr/share/gtk-doc/html/libmbim-glib/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmbim-glib.so.4
/usr/lib64/libmbim-glib.so.4.4.1

%files libexec
%defattr(-,root,root,-)
/usr/libexec/mbim-proxy

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libmbim/COPYING
/usr/share/package-licenses/libmbim/COPYING.LIB

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mbim-network.1
/usr/share/man/man1/mbimcli.1
