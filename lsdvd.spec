Summary:	List dvd's content
Summary(pl):	Pokazywanie zawarto¶ci dvd
Name:		lsdvd
Version:	0.16
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://dl.sourceforge.net/acidrip/%{name}-%{version}.tar.gz
# Source0-md5:	0dbb395f73aeec4b08d8997d07df287b
Patch0:		%{name}-stdint.patch
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
Lsdvd pozwala na sprawdzenie zawarto¶ci DVD oraz podaje informacje na
temat poszczególnych ¶cie¿ek, takie jak ilo¶æ i rodzaje ¶cie¿ek audio
czy napisów itd. Nieoceniony w sytuacji kiedy chcemy odtwarzaæ lub
przekodowaæ film, który jest gdzie¶ g³êboko ukryty po¶ród dziesi±tek
bezu¿ytecznych ¶cie¿ek z czo³ówkami i trailerami.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/lsdvd
%{_mandir}/man1/lsdvd.1*
