Summary:	Wireless network assistant
Summary(pl):	Asystent sieci bezprzewodowej
Name:		wlassistant
Version:	0.3.9
Release:	1
License:	GPL v2
Group:		X11/Applications	
Source0:	http://dl.sourceforge.net/wlassistant/%{name}-%{version}.tar.bz2
# Source0-md5:	fd414931788e1c95fc9af5f99c22a042
URL:		http://wlassistant.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	qt-devel
BuildRequires:	zlib-devel
Requires:	dhcpcd
Requires:	wireless-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wireless network assistant.

%description -l pl
Asystent sieci bezprzewodowej.

%prep
%setup -q

%build
%{__make} -f Makefile.cvs
%configure \
%if "%{_lib}" == "lib64"
        --enable-libsuffix=64
%endif

%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
# -> %{_desktopdir}
#%{_datadir}/applnk/Utilities/wlassistant.desktop
%{_datadir}/apps/wlassistant
%{_datadir}/config.kcfg/waconfig.kcfg
%{_datadir}/icons/*/*x*/apps/wlassistant.png
