Summary:	Virtuozzo/OpenVZ disk quota control utility
Summary(pl.UTF-8):	Narzędzie do sterowania limitami dyskowymi Virtuozzo/OpenVZ
Name:		vzquota
Version:	3.1
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://download.openvz.org/utils/vzquota/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	a3c837999a90381ba028ee73e84f40f2
Patch0:		vzquota.patch
Patch1:		time_t.patch
URL:		http://openvz.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility allows system administator to control disk quotas for
Virtuozzo/OpenVZ containers.

%description -l pl.UTF-8
To narzędzie pozwala administratorowi systemu sterować limitami
dyskowymi (quota) dla kontenerów Virtuozzo/OpenVZ.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	DEBUG="%{rpmcflags} %{rpmldflags}" \
	VARDIR=/var/lib

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	VARDIR=/var/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_sbindir}/vzquota
%attr(755,root,root) %{_sbindir}/vzdqcheck
%attr(755,root,root) %{_sbindir}/vzdqdump
%attr(755,root,root) %{_sbindir}/vzdqload
%{_mandir}/man8/vzquota.8*
%{_mandir}/man8/vzdqcheck.8*
%{_mandir}/man8/vzdqdump.8*
%{_mandir}/man8/vzdqload.8*
%dir %{_var}/lib/vzquota
