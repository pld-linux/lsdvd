Summary:	list dvd's content
Summary(pl):	pokazuje zawarto¶æ dvd
Name:		lsdvd
Version:	0.6
Release:	0.1
License:	GPL
Group:		Applications/File
Source0:	http://prdownloads.sourceforge.net/acidrip/%{name}-%{version}.tar.gz
URL:		http://acidrip.thirtythreeandathird.net/lsdvd.html
BuildRequires:	libdvdread-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
