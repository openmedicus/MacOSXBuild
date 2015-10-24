Name:           darwinx-gdl
Version:        3.14.0
Release:        1%{?dist}
Summary:        Mac OS X GDL library

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gdl/3.14/gdl-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 15
BuildRequires:  darwinx-gcc

BuildRequires:  darwinx-atk
BuildRequires:  darwinx-cairo
BuildRequires:  darwinx-gdk-pixbuf
BuildRequires:  darwinx-gettext
BuildRequires:  darwinx-glib2
BuildRequires:  darwinx-gtk3
BuildRequires:  darwinx-pango
BuildRequires:  darwinx-pixman

%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

%prep
%setup -q -n gdl-%{version}

%build
%{_darwinx_configure}

%{_darwinx_make} %{?_smp_mflags} V=1


%install
%{_darwinx_make} install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_darwinx_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_darwinx_libdir}/locale
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc

%files -n darwinx-gdl
%doc COPYING
%{_darwinx_libdir}/libgdl-3.5.dylib
%{_darwinx_libdir}/libgdl-3.dylib
%{_darwinx_includedir}/libgdl-3.0/gdl/gdl-dock-bar.h
%dir %{_darwinx_includedir}/libgdl-3.0
%dir %{_darwinx_includedir}/libgdl-3.0/gdl
%{_darwinx_includedir}/libgdl-3.0/gdl/gdl-dock.h
%{_darwinx_includedir}/libgdl-3.0/gdl/gdl-dock-item-grip.h
%{_darwinx_includedir}/libgdl-3.0/gdl/gdl-dock-item.h
%{_darwinx_includedir}/libgdl-3.0/gdl/gdl-dock-layout.h
%{_darwinx_includedir}/libgdl-3.0/gdl/gdl-dock-master.h
%{_darwinx_includedir}/libgdl-3.0/gdl/gdl-dock-object.h
%{_darwinx_includedir}/libgdl-3.0/gdl/gdl-dock-placeholder.h
%{_darwinx_includedir}/libgdl-3.0/gdl/gdl.h
%{_darwinx_includedir}/libgdl-3.0/gdl/libgdltypebuiltins.h
%{_darwinx_libdir}/pkgconfig/gdl-3.0.pc

%changelog
* Tue Nov 04 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.12.0-1
- Initial RPM release
