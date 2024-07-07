Name:           libjpeg8
Version:        2.1.4
Release:        1%{?dist}
Summary:        A MMX/SSE2/SIMD accelerated library for manipulating JPEG image files
License:        IJG
URL:            http://sourceforge.net/projects/libjpeg-turbo

Source0:        http://downloads.sourceforge.net/libjpeg-turbo/libjpeg-turbo-%{version}.tar.gz
Patch0:         libjpeg-turbo-cmake.patch
Patch1:         libjpeg-turbo-CET.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  libtool
BuildRequires:  nasm

%description
Compatibiliyy libjpeg v8 API/ABI library through libjpeg-turbo.

%prep
%autosetup -p1 -n libjpeg-turbo-%{version}

%build
# NASM object files are missing GNU Property note for Intel CET,
# force it on the resulting library
%ifarch %{ix86} x86_64
export LDFLAGS="$RPM_LD_FLAGS -Wl,-z,ibt -Wl,-z,shstk"
%endif

%{cmake} \
    -DCMAKE_SKIP_RPATH:BOOL=YES \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
    -DENABLE_STATIC:BOOL=NO \
    -DWITH_JPEG8:BOOL=YES \
    -DWITH_TURBOJPEG:BOOL=NO

%cmake_build

%install
mkdir -p %{buildroot}%{_libdir}
install -m 0755 -p %{_vpath_builddir}/libjpeg.so.* %{buildroot}%{_libdir}

%files
%{_libdir}/libjpeg.so.*

%changelog
* Sat Jul 06 2024 Simone Caronni <negativo17@gmail.com> - 2.1.4-1
- First build.
