# TODO: don't put functions.pm in perl_vendorlib
%include	/usr/lib/rpm/macros.perl
%define		_mainver	0.7
%define		_subver	.5
%define		_ver	%(echo %{_subver} |tr . -)
Summary:	dvd2avi - conversion tool
Summary(de):	dvd2avi - ein konversions Tool
Summary(pl):	dvd2avi - narzêdzie do konwersji
Name:		dvd2avi
Version:	%{_mainver}%{_subver}
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/dvd2avi/%{name}-%{_mainver}%{_ver}.tgz
# Source0-md5:	26ecb079c5ee49a4025c3a1323b2daa6
Source1:	%{name}.desktop
Patch0:		%{name}-location.patch
URL:		http://dvd2avi.sourceforge.net/
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DVD2AVI makes conversion of DVDs to AVIs a real breeze.

%description -l de
DVD2AVI macht eine konversion von einer DVD zum AVI Format zum
Kinderspiel.

%description -l pl
DVD2AVI sprawia, ¿e konwersja z DVD do AVI staje siê lekka jak morska
bryza.

%prep
%setup -q -n opt/%{name}
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{perl_vendorarch},%{_datadir}/dvd2avi,%{_desktopdir}}
install dvd2avi $RPM_BUILD_ROOT%{_bindir}/dvd2avi
install functions.pm $RPM_BUILD_ROOT%{perl_vendorarch}/functions.pm
install dvd2avi.glade $RPM_BUILD_ROOT%{_datadir}/dvd2avi/dvd2avi.glade
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README INSTALL
%attr(755,root,root) %{_bindir}/dvd2avi
%{perl_vendorarch}/functions.pm
%dir %{_datadir}/dvd2avi
%{_datadir}/dvd2avi/dvd2avi.glade
%{_desktopdir}/dvd2avi.desktop
