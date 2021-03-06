#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBA88000FE6398272 (mzidek@redhat.com)
#
Name     : ding-libs
Version  : 0.6.1
Release  : 4
URL      : https://releases.pagure.org/SSSD/ding-libs/ding-libs-0.6.1.tar.gz
Source0  : https://releases.pagure.org/SSSD/ding-libs/ding-libs-0.6.1.tar.gz
Source1  : https://releases.pagure.org/SSSD/ding-libs/ding-libs-0.6.1.tar.gz.asc
Summary  : A data-type to collect data in a heirarchical structure for easy iteration and serialization
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: ding-libs-lib = %{version}-%{release}
Requires: ding-libs-license = %{version}-%{release}
BuildRequires : pkgconfig(check)
Patch1: INI-Silence-ini_augment-match-failures.patch
Patch2: INI-Remove-definiton-of-TRACE_LEVEL.patch
Patch3: INI-Fix-detection-of-error-messages.patch
Patch4: TEST-validators_ut_check-Fix-fail-with-new-glibc.patch

%description
To build the ding-libs from the tarball:
./configure
make
make docs (optional)
make check (optional)
make install

%package dev
Summary: dev components for the ding-libs package.
Group: Development
Requires: ding-libs-lib = %{version}-%{release}
Provides: ding-libs-devel = %{version}-%{release}
Requires: ding-libs = %{version}-%{release}

%description dev
dev components for the ding-libs package.


%package doc
Summary: doc components for the ding-libs package.
Group: Documentation

%description doc
doc components for the ding-libs package.


%package lib
Summary: lib components for the ding-libs package.
Group: Libraries
Requires: ding-libs-license = %{version}-%{release}

%description lib
lib components for the ding-libs package.


%package license
Summary: license components for the ding-libs package.
Group: Default

%description license
license components for the ding-libs package.


%prep
%setup -q -n ding-libs-0.6.1
cd %{_builddir}/ding-libs-0.6.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579033728
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1579033728
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ding-libs
cp %{_builddir}/ding-libs-0.6.1/COPYING %{buildroot}/usr/share/package-licenses/ding-libs/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/ding-libs-0.6.1/COPYING.LESSER %{buildroot}/usr/share/package-licenses/ding-libs/978773e74b4cfcbe611ae1217754f259ad37ac96
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/collection.h
/usr/include/collection_queue.h
/usr/include/collection_stack.h
/usr/include/collection_tools.h
/usr/include/dhash.h
/usr/include/ini_comment.h
/usr/include/ini_config.h
/usr/include/ini_configmod.h
/usr/include/ini_configobj.h
/usr/include/ini_valueobj.h
/usr/include/path_utils.h
/usr/include/ref_array.h
/usr/include/simplebuffer.h
/usr/lib64/libbasicobjects.so
/usr/lib64/libcollection.so
/usr/lib64/libdhash.so
/usr/lib64/libini_config.so
/usr/lib64/libpath_utils.so
/usr/lib64/libref_array.so
/usr/lib64/pkgconfig/basicobjects.pc
/usr/lib64/pkgconfig/collection.pc
/usr/lib64/pkgconfig/dhash.pc
/usr/lib64/pkgconfig/ini_config.pc
/usr/lib64/pkgconfig/path_utils.pc
/usr/lib64/pkgconfig/ref_array.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/ding\-libs/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbasicobjects.so.0
/usr/lib64/libbasicobjects.so.0.1.0
/usr/lib64/libcollection.so.4
/usr/lib64/libcollection.so.4.1.1
/usr/lib64/libdhash.so.1
/usr/lib64/libdhash.so.1.1.0
/usr/lib64/libini_config.so.5
/usr/lib64/libini_config.so.5.2.1
/usr/lib64/libpath_utils.so.1
/usr/lib64/libpath_utils.so.1.0.1
/usr/lib64/libref_array.so.1
/usr/lib64/libref_array.so.1.2.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ding-libs/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/ding-libs/978773e74b4cfcbe611ae1217754f259ad37ac96
