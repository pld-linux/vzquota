# TODO
# - not FHS compliant /var/vzquota
Summary:	Virtuozzo/OpenVZ disk quota control utility
Name:		vzquota
Version:	3.0.12
Release:	2
License:	GPL v2
Group:		Base/Kernel
Source0:	http://download.openvz.org/utils/vzquota/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	d45e49f90c38c70a46f08deecb387377
Patch0:		vzdqload.patch
URL:		http://openvz.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility allows system administator to control disk quotas for
Virtuozzo/OpenVZ containers.

%prep
%setup -q
%patch0 -p0

%build
%{__make} \
	CC="%{__cc}" \
	DEBUG="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%dir %{_var}/vzquota
