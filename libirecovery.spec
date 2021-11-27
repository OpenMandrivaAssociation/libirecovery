%define major	3
%define api	1.0

%define libname %mklibname irecovery %{api} %{major}
%define devname %mklibname -d irecovery

%define	git	20211124

Summary:	Library for manipulating Apple Binary and XML Property Lists
Name:		libirecovery
Version:	1.0.1
Release:	1.%{git}.0
Group:		System/Libraries
License:	LGPLv2+
Url:		http://www.libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.xz
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

%build
autoreconf -fiv

%configure \
	--disable-static \
	--with-udevrulesdir=%{_udevrulesdir}
	
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



