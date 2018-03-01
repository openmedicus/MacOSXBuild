%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name PDFsharp-MigraDoc
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /lib
%define apiversion 1.50.0.0

%define beta -beta5

Name:           mingw-PDFsharp-MigraDoc
Version:        1.50.4740
Release:        beta5%{?dist}
Summary:        .NET library that easily creates documents and renders them into PDF or RTF.

Group:          Development/Languages
License:        MIT
URL:            http://www.pdfsharp.net
Prefix:		/usr

BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

%description
MigraDoc Foundation - the Open Source .NET library that easily creates documents based on an 
object model with paragraphs, tables, styles, etc. and renders them into PDF or RTF.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw32-mono-core

%description -n mingw32-%{mingw_pkg_name}
MigraDoc Foundation - the Open Source .NET library that easily creates documents based on an
object model with paragraphs, tables, styles, etc. and renders them into PDF or RTF.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw64-mono-core

%description -n mingw64-%{mingw_pkg_name}
MigraDoc Foundation - the Open Source .NET library that easily creates documents based on an
object model with paragraphs, tables, styles, etc. and renders them into PDF or RTF.

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}%{beta}

cat > %{mingw_pkg_name}32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}/mono/%{mingw_pkg_name}

Name: %{mingw_pkg_name}
Description: %{mingw_pkg_name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/PdfSharp.dll -r:${libdir}/PdfSharp.Charting.dll -r:${libdir}/MigraDoc.RtfRendering.dll -r:${libdir}/MigraDoc.Rendering.dll -r:${libdir}/MigraDoc.DocumentObjectModel.dll
Cflags:
EOF

cat > %{mingw_pkg_name}64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}/mono/%{mingw_pkg_name}

Name: %{mingw_pkg_name}
Description: %{mingw_pkg_name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/PdfSharp.dll -r:${libdir}/PdfSharp.Charting.dll -r:${libdir}/MigraDoc.RtfRendering.dll -r:${libdir}/MigraDoc.Rendering.dll -r:${libdir}/MigraDoc.DocumentObjectModel.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
gacutil -i %{mingw_pkg_name}.%{version}%{beta}/lib/net20/MigraDoc.DocumentObjectModel.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac
gacutil -i %{mingw_pkg_name}.%{version}%{beta}/lib/net20/MigraDoc.Rendering.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac
gacutil -i %{mingw_pkg_name}.%{version}%{beta}/lib/net20/MigraDoc.RtfRendering.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac
gacutil -i %{mingw_pkg_name}.%{version}%{beta}/lib/net20/PdfSharp.Charting.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac
gacutil -i %{mingw_pkg_name}.%{version}%{beta}/lib/net20/PdfSharp.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 %{mingw_pkg_name}32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/%{mingw_pkg_name}.pc

# Mingw64
gacutil -i %{mingw_pkg_name}.%{version}%{beta}/lib/net20/MigraDoc.DocumentObjectModel.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac
gacutil -i %{mingw_pkg_name}.%{version}%{beta}/lib/net20/MigraDoc.Rendering.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac
gacutil -i %{mingw_pkg_name}.%{version}%{beta}/lib/net20/MigraDoc.RtfRendering.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac
gacutil -i %{mingw_pkg_name}.%{version}%{beta}/lib/net20/PdfSharp.Charting.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac
gacutil -i %{mingw_pkg_name}.%{version}%{beta}/lib/net20/PdfSharp.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 %{mingw_pkg_name}64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/%{mingw_pkg_name}.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/mono/gac
%{mingw32_prefix}%{libdir}/mono/%{mingw_pkg_name}/MigraDoc.DocumentObjectModel.dll
%{mingw32_prefix}%{libdir}/mono/%{mingw_pkg_name}/MigraDoc.Rendering.dll
%{mingw32_prefix}%{libdir}/mono/%{mingw_pkg_name}/MigraDoc.RtfRendering.dll
%{mingw32_prefix}%{libdir}/mono/%{mingw_pkg_name}/PdfSharp.Charting.dll
%{mingw32_prefix}%{libdir}/mono/%{mingw_pkg_name}/PdfSharp.dll
%{mingw32_datadir}/pkgconfig/%{mingw_pkg_name}.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/mono/gac
%{mingw64_prefix}%{libdir}/mono/%{mingw_pkg_name}/MigraDoc.DocumentObjectModel.dll
%{mingw64_prefix}%{libdir}/mono/%{mingw_pkg_name}/MigraDoc.Rendering.dll
%{mingw64_prefix}%{libdir}/mono/%{mingw_pkg_name}/MigraDoc.RtfRendering.dll
%{mingw64_prefix}%{libdir}/mono/%{mingw_pkg_name}/PdfSharp.Charting.dll
%{mingw64_prefix}%{libdir}/mono/%{mingw_pkg_name}/PdfSharp.dll
%{mingw64_datadir}/pkgconfig/%{mingw_pkg_name}.pc

%changelog
* Thu Jan 4 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.50.4740-beta5-1
- Initial version