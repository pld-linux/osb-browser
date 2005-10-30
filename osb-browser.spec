Summary:	GTK-Webcore Browser
Summary(pl):	Przegl±darka GTK-Webcore
Name:		osb-browser
Version:	0.5.0
Release:	0.1
License:	GPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/gtk-webcore/%{name}-%{version}.tar.gz
# Source0-md5:	4dad43f6e1291dfefaec6e9209928a0d
URL:		http://gtk-webcore.sourceforge.net/
BuildRequires:	gtk+2-devel
BuildRequires:	osb-jscore-devel
BuildRequires:	osb-nrcore-devel
BuildRequires:	osb-nrcit-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK Webcore Browser.

%description -l pl
Przegl±darka GTK Webcore.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/osb-browser
%{_datadir}/%{name}
