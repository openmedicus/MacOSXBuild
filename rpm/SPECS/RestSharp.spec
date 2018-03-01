%define debug_package %{nil}

%define platform net45
%define libdir /lib

Name:		RestSharp
Version: 	105.2.3
Release: 	1%{?dist}
Summary: 	Simple REST and HTTP API Client
Group: 		System Environment/Libraries
License: 	Apache License
URL:		http://sourceforge.net/projects/sharpssh/
Source0: 	Apache-LICENSE.txt
BuildArch:      noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr

BuildRequires:	nuget
Requires:	mono-core

%description
Simple REST and HTTP API Client

%prep
%setup -c %{name}-%{version} -T
nuget install %{name}Signed -Version %{version}

cat > RestSharp.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{libdir}/mono/RestSharp

Name: RestSharp
Description: Simple REST and HTTP API Client
Requires: 
Version: %{version}
Libs: -r:${libdir}/RestSharp.dll
Cflags:
EOF

%build

%install  
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/mono/gac
gacutil -i RestSharpSigned.%{version}/lib/net45/RestSharp.dll -package RestSharp -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

#install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/mono/RestSharp
#install -m 644 RestSharpSigned.%{version}/lib/net45/RestSharp.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/mono/RestSharp/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/RestSharp
install -m 664 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/RestSharp/License

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig
install -m 644 RestSharp.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/RestSharp.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%{_datadir}/RestSharp/License
%{_prefix}%{libdir}/mono/gac
%{_prefix}%{libdir}/mono/RestSharp/RestSharp.dll
%{_datadir}/pkgconfig/RestSharp.pc

%changelog
* Fri Nov 24 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- first draft of spec file
