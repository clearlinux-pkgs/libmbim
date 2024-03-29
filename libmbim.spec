#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0x3CAD53398973FFFA (aleksander@aleksander.es)
#
Name     : libmbim
Version  : 1.26.4
Release  : 22
URL      : https://www.freedesktop.org/software/libmbim/libmbim-1.26.4.tar.xz
Source0  : https://www.freedesktop.org/software/libmbim/libmbim-1.26.4.tar.xz
Source1  : https://www.freedesktop.org/software/libmbim/libmbim-1.26.4.tar.xz.asc
Summary  : Library to communicate with MBIM-powered modems
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libmbim-bin = %{version}-%{release}
Requires: libmbim-data = %{version}-%{release}
Requires: libmbim-lib = %{version}-%{release}
Requires: libmbim-libexec = %{version}-%{release}
Requires: libmbim-license = %{version}-%{release}
Requires: libmbim-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : docbook-xml
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n libmbim-1.26.4
cd %{_builddir}/libmbim-1.26.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702019392
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1702019392
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libmbim
cp %{_builddir}/libmbim-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libmbim/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/libmbim-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/libmbim/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mbim-network
/usr/bin/mbimcli

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Mbim-1.0.typelib
/usr/share/bash-completion/completions/mbimcli
/usr/share/gir-1.0/*.gir

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
/usr/include/libmbim-glib/mbim-ms-sar.h
/usr/include/libmbim-glib/mbim-ms-uicc-low-level-access.h
/usr/include/libmbim-glib/mbim-phonebook.h
/usr/include/libmbim-glib/mbim-proxy-control.h
/usr/include/libmbim-glib/mbim-proxy.h
/usr/include/libmbim-glib/mbim-qdu.h
/usr/include/libmbim-glib/mbim-qmi.h
/usr/include/libmbim-glib/mbim-quectel.h
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
/usr/share/gtk-doc/html/libmbim-glib/api-index-1-0.html
/usr/share/gtk-doc/html/libmbim-glib/api-index-1-10.html
/usr/share/gtk-doc/html/libmbim-glib/api-index-1-12.html
/usr/share/gtk-doc/html/libmbim-glib/api-index-1-14.html
/usr/share/gtk-doc/html/libmbim-glib/api-index-1-16.html
/usr/share/gtk-doc/html/libmbim-glib/api-index-1-18.html
/usr/share/gtk-doc/html/libmbim-glib/api-index-1-2.html
/usr/share/gtk-doc/html/libmbim-glib/api-index-1-24-4.html
/usr/share/gtk-doc/html/libmbim-glib/api-index-1-24.html
/usr/share/gtk-doc/html/libmbim-glib/api-index-1-26-2.html
/usr/share/gtk-doc/html/libmbim-glib/api-index-1-26.html
/usr/share/gtk-doc/html/libmbim-glib/api-index-1-4.html
/usr/share/gtk-doc/html/libmbim-glib/api-index-1-8.html
/usr/share/gtk-doc/html/libmbim-glib/api-index-deprecated.html
/usr/share/gtk-doc/html/libmbim-glib/api-index-full.html
/usr/share/gtk-doc/html/libmbim-glib/ch01.html
/usr/share/gtk-doc/html/libmbim-glib/ch02.html
/usr/share/gtk-doc/html/libmbim-glib/ch03.html
/usr/share/gtk-doc/html/libmbim-glib/ch04.html
/usr/share/gtk-doc/html/libmbim-glib/ch05.html
/usr/share/gtk-doc/html/libmbim-glib/ch06.html
/usr/share/gtk-doc/html/libmbim-glib/ch07.html
/usr/share/gtk-doc/html/libmbim-glib/ch08.html
/usr/share/gtk-doc/html/libmbim-glib/ch09.html
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
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-MS-SAR.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-MS-UICC-Low-Level-Access.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-Ms-Basic-Connect-Extensions.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-Phonebook.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-Proxy-Control.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-QDU.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-QMI.html
/usr/share/gtk-doc/html/libmbim-glib/libmbim-glib-Quectel.html
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
/usr/lib64/libmbim-glib.so.4.6.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/mbim-proxy

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libmbim/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/libmbim/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mbim-network.1
/usr/share/man/man1/mbimcli.1
