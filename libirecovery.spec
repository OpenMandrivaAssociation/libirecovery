%define major	3
%define api	1.0

%define oldlibname %mklibname irecovery %{api} 3
%define libname %mklibname irecovery %{api}
%define devname %mklibname -d irecovery

#define	git	20230802

Summary:	Library for manipulating Apple Binary and XML Property Lists
Name:		libirecovery
Version:	1.1.0
Release:	%{?git:0.%{git}.}1
Group:		System/Libraries
License:	LGPLv2+
Url:		https://www.libimobiledevice.org/
%if 0%{?git:1}
Source0:	https://github.com/libimobiledevice/libirecovery/archive/refs/heads/master.tar.gz#/%{name}-%{git}.tar.gz
%else
Source0:	https://github.com/libimobiledevice/libirecovery/releases/download/%{version}/libirecovery-%{version}.tar.bz2
%endif
BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(libimobiledevice-glue-1.0)
BuildRequires:	pkgconfig(libusb-1.0)

%description
libirecovery is a cross-platform library which implements communication to
iBoot/iBSS found on Apple's iOS devices via USB. 
A command-line utility named irecovery is available as a separate package.

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for accessing Apple's iBoot/IBSS via usb 
Suggests:	%{name} >= %{version}-%{release}
%rename %{oldlibname}

%description -n %{libname}
irecovery is a library allowing access to to Apples iBoot/IBSS via usb

%package -n %{devname}
Summary:	Development package for libirecovery
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
%{name}, development headers and libraries.

%package -n irecovery
Group:		System/Tools
Summary:	Tool to access iboot/iBSS over usb on IOS devices
Requires:	%{libname} = %{version}-%{release}

%description -n irecovery
irecovery is a cross-platform tool which allows communication via USB to
iBoot/iBSS that are found on Apple's iOS devices

%prep
%autosetup -p1
autoreconf -fiv

%configure \
	--disable-static \
	--with-udevrulesdir=%{_udevrulesdir}

%build
%make_build

%install
%make_install

%files -n %{libname} 
%doc NEWS README.md COPYING
%{_libdir}/%{name}-%{api}.so.%{major}{,.*}

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/%{name}-%{api}.so

%files -n irecovery
%{_bindir}/irecovery
%{_udevrulesdir}/39-libirecovery.rules
