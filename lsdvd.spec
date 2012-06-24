Summary:	List dvd's content
Summary(pl):	Pokazywanie zawarto�ci dvd
Name:		lsdvd
Version:	0.15
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://dl.sourceforge.net/acidrip/%{name}-%{version}.tar.gz
# Source0-md5:	5ea6a942804cfc7911e7a0efe4819c7a
URL:		http://untrepid.com/acidrip/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdvdread-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lsdvd allows to check the contents of the DVD as well as information
about particular tracks such as audio and subtitle languages etc.
Priceless when you want to play or rip video which is somewhere among
the dozens of useless promotional/trailer tracks.

%description -l pl
Lsdvd pozwala na sprawdzenie zawarto�ci DVD oraz podaje informacje na
temat poszczeg�lnych �cie�ek, takie jak ilo�� i rodzaje �cie�ek audio
czy napis�w itd. Nieoceniony w sytuacji kiedy chcemy odtwarza� lub
przekodowa� film, kt�ry jest gdzie� g��boko ukryty po�r�d dziesi�tek
bezu�ytecznych �cie�ek z czo��wkami i trailerami.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%attr(755,root,root) %{_bindir}/*
