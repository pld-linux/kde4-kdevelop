#
# Conditional build:
#
%define		_state		stable
%define		kdever		4.12.0
%define		qtver		4.8.0
%define		orgname		kdevelop
%define		kdevplatform	1.7.0

Summary:	KDE Integrated Development Environment
Summary(de.UTF-8):	KDevelop ist eine grafische Entwicklungsumgebung für KDE
Summary(pl.UTF-8):	Zintegrowane środowisko programisty dla KDE
Summary(pt_BR.UTF-8):	Ambiente Integrado de Desenvolvimento para o KDE
Summary(zh_CN.UTF-8):	KDE C/C++集成开发环境
Name:		kde4-kdevelop
Version:	4.7.0
Release:	0.3
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/kdevelop/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	0912f881cb1219450aeb155494846bbd
URL:		http://www.kdevelop.org/
BuildRequires:	QtHelp-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.8.0
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdebase-workspace-devel >= 4.10.0
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
# BuildRequires:	kde4-kde-dev-utils >= %{kdever}
#BuildRequires:	kde4-kde-dev-scripts >= %{kdever}
# BuildRequires:	kde4-kapptemplate >= %{kdever}
# BuildRequires:	kde4-kcachegrind >= %{kdever}
#BuildRequires:	kde4-kdesdk-kioslaves >= %{kdever}
#BuildRequires:	kde4-kdesdk-strigi-analyzers >= %{kdever}
#BuildRequires:	kde4-kdesdk-thumbnailers >= %{kdever}
#BuildRequires:	kde4-kompare >= %{kdever}
#BuildRequires:	kde4-lokalize >= %{kdever}
BuildRequires:	kde4-okteta-devel >= %{kdever}
#BuildRequires:	kde4-poxml >= %{kdever}
# BuildRequires:	kde4-umbrello >= %{kdever}
BuildRequires:	kde4-kdevplatform-devel >= %{kdevplatform}
BuildRequires:	libstdc++-devel >= 3.3
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	zlib-devel >= 1.2.0
BuildConflicts:	star
Requires:	libstdc++-gdb
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         filterout       -flto

%description
The KDevelop Integrated Development Environment provides many features
that developers need as well as providing a unified interface to
programs like gdb, the C/C++ compiler, and make.

KDevelop manages or provides: all development tools needed for C++
programming like Compiler, Linker, automake and autoconf; KAppWizard,
which generates complete, ready-to-go sample applications;
Classgenerator, for creating new classes and integrating them into the
current project; File management for sources, headers, documentation
etc. to be included in the project; The creation of User-Handbooks
written with SGML and the automatic generation of HTML-output with the
KDE look and feel; Automatic HTML-based API-documentation for your
project's classes with cross-references to the used libraries;
Internationalization support for your application, allowing
translators to easily add their target language to a project;

KDevelop also includes WYSIWYG (What you see is what you get)-creation
of user interfaces with a built-in dialog editor; Debugging your
application by integrating KDbg; Editing of project-specific pixmaps
with KIconEdit; The inclusion of any other program you need for
development by adding it to the "Tools"-menu according to your
individual needs.

%description -l de.UTF-8
KDevelop ist eine grafische Entwicklungsumgebung für KDE.

Das KDevelop-Projekt wurde 1998 begonnen, um eine einfach zu
bedienende grafische (integrierte) Entwicklungsumgebung für C++ und C
auf Unix-basierten Betriebssystemen bereitzustellen. Seit damals ist
die KDevelop-IDE öffentlich unter der GPL erhältlich und unterstützt
u. a. Qt-, KDE-, GNOME-, C++- und C-Projekte.

%description -l pl.UTF-8
KDevelop to zintegrowane środowisko programistyczne dla KDE, dające
wiele możliwości przydatnych programistom oraz zunifikowany interfejs
do programów typu gdb, kompilator C/C++ oraz make.

KDevelop obsługuje lub zawiera: wszystkie narzędzia programistyczne
potrzebne do programowania w C++ jak kompilator, linker, automake,
autoconf; KAppWizard, generujący kompletne, gotowe do uruchomienia,
proste aplikacje; Classgenerator do tworzenia nowych klas i włączania
ich do projektu; zarządzanie plikami źródłowymi, nagłówkowymi,
dokumentacją itp.; tworzenie podręczników użytkownika pisanych w SGML
i automatyczne generowanie wyjścia HTML pasującego do KDE;
automatyczne tworzenie dokumentacji API w HTML do klas projektu z
odniesieniami do używanych bibliotek; wsparcie dla
internacjonalizacji, pozwalające tłumaczom łatwo dodawać pliki z
tłumaczeniami do projektu.

KDevelop ma także tworzenie interfejsów użytkownika przy użyciu
edytora dialogów WYSIWYG; odpluskwianie aplikacji poprzez integrację z
KDbg; edycję ikon przy pomocy KIconEdit; dołączanie innych programów
potrzebnych do programowania przez dodanie ich do menu Tools według
własnych potrzeb.

%package devel
Summary:	kdevelop - header files and development documentation
Summary(pl.UTF-8):	kdevelop - pliki nagłówkowe i dokumentacja
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files and development documentation for
kdevelop.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących kdevelop.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install app/kdevelop.desktop $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{orgname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_mime_database
%update_desktop_database

%postun
/sbin/ldconfig
%update_mime_database
%update_desktop_database_postun

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdevelop
%attr(755,root,root) %{_bindir}/kdevelop!
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_makebuilder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_cmakebuilder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdevcmake_settings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_ninjabuilder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdevcustombuildsystem.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdevcustomdefinesandincludes.so
%attr(755,root,root) %{_libdir}/kde4/kdevastyle.so
%attr(755,root,root) %{_libdir}/kde4/kdevcmakebuilder.so
%attr(755,root,root) %{_libdir}/kde4/kdevcmakedocumentation.so
%attr(755,root,root) %{_libdir}/kde4/kdevcmakemanager.so
%attr(755,root,root) %{_libdir}/kde4/kdevcompilerprovider.so
%attr(755,root,root) %{_libdir}/kde4/kdevcpplanguagesupport.so
%attr(755,root,root) %{_libdir}/kde4/kdevcustombuildsystem.so
%attr(755,root,root) %{_libdir}/kde4/kdevcustommakemanager.so
%attr(755,root,root) %{_libdir}/kde4/kdevcustomscript.so
%attr(755,root,root) %{_libdir}/kde4/kdevdefinesandincludesmanager.so
%attr(755,root,root) %{_libdir}/kde4/kdevexecuteplasmoid.so
%attr(755,root,root) %{_libdir}/kde4/kdevgdb.so
%attr(755,root,root) %{_libdir}/kde4/kdevghprovider.so
%attr(755,root,root) %{_libdir}/kde4/kdevokteta.so
%attr(755,root,root) %{_libdir}/kde4/kdevmakebuilder.so
%attr(755,root,root) %{_libdir}/kde4/kdevmanpage.so
%attr(755,root,root) %{_libdir}/kde4/kdevninja.so
%attr(755,root,root) %{_libdir}/kde4/kdevqthelp.so
%attr(755,root,root) %{_libdir}/kde4/kdevqthelp_config.so
%attr(755,root,root) %{_libdir}/kde4/kdevkdeprovider.so
%attr(755,root,root) %{_libdir}/kde4/krunner_kdevelopsessions.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_kdevelopsessions.so
%attr(755,root,root) %{_libdir}/libkdev4cmakecommon.so
%attr(755,root,root) %{_libdir}/libkdev4cppduchain.so
%attr(755,root,root) %{_libdir}/libkdev4cppparser.so
%attr(755,root,root) %{_libdir}/libkdev4cpprpp.so
%attr(755,root,root) %{_libdir}/libkdev4includesdefinessettings.so
%{_datadir}/apps/kdevappwizard
%{_datadir}/apps/kdevcodegen/templates/*
%{_datadir}/apps/kdevcustommakemanager
%{_datadir}/apps/kdevelop
%{_datadir}/apps/kdevfiletemplates/templates/*
%dir %{_datadir}/apps/kdevgdb
%{_datadir}/apps/kdevgdb/kdevgdbui.rc
%dir %{_datadir}/apps/kdevgdb/printers
%{_datadir}/apps/kdevgdb/printers/gdbinit
%{_datadir}/apps/kdevgdb/printers/helper.py
%{_datadir}/apps/kdevgdb/printers/qt4.py
%{_datadir}/apps/kdevgdb/printers/kde4.py
%dir %{_datadir}/apps/kdevmanpage
%{_datadir}/apps/kdevmanpage/manpagedocumentation.css
%{_datadir}/apps/kdevokteta
%{_datadir}/apps/plasma/plasmoids/kdevelopsessions
%{_datadir}/apps/plasma/services/org.kde.plasma.dataengine.kdevelopsessions.operations
%{_datadir}/config/kdeveloprc
%{_datadir}/config/kdevelop-qthelp.knsrc
%dir %{_datadir}/apps/kdevcppsupport
%{_datadir}/apps/kdevcppsupport/kdevcppsupport.rc
%{_datadir}/kde4/services/kcm_kdev_cmakebuilder.desktop
%{_datadir}/kde4/services/kcm_kdev_makebuilder.desktop
%{_datadir}/kde4/services/kcm_kdevcmake_settings.desktop
%{_datadir}/kde4/services/kcm_kdev_ninjabuilder.desktop
%{_datadir}/kde4/services/kcm_kdevcustombuildsystem.desktop
%{_datadir}/kde4/services/kcm_kdevcustomdefinesandincludes.desktop
%{_datadir}/kde4/services/kdevastyle.desktop
%{_datadir}/kde4/services/kdevcmakebuilder.desktop
%{_datadir}/kde4/services/kdevcmakedocumentation.desktop
%{_datadir}/kde4/services/kdevcmakemanager.desktop
%{_datadir}/kde4/services/kdevcompilerprovider.desktop
%{_datadir}/kde4/services/kdevcustombuildsystem.desktop
%{_datadir}/kde4/services/kdevcustomscript.desktop
%{_datadir}/kde4/services/kdevcppsupport.desktop
%{_datadir}/kde4/services/kdevcustommakemanager.desktop
%{_datadir}/kde4/services/kdevdefinesandincludesmanager.desktop
%{_datadir}/kde4/services/kdevexecuteplasmoid.desktop
%{_datadir}/kde4/services/kdevgdb.desktop
%{_datadir}/kde4/services/kdevghprovider.desktop
%{_datadir}/kde4/services/kdevmakebuilder.desktop
%{_datadir}/kde4/services/kdevmanpage.desktop
%{_datadir}/kde4/services/kdevninja.desktop
%{_datadir}/kde4/services/kdevokteta.desktop
%{_datadir}/kde4/services/kdevqthelp.desktop
%{_datadir}/kde4/services/kdevqthelp_config.desktop
%{_datadir}/kde4/services/kdevelopsessions.desktop
%{_datadir}/kde4/services/kdevkdeprovider.desktop
%{_datadir}/kde4/services/plasma-applet-kdevelopsessions.desktop
%{_datadir}/kde4/services/plasma-dataengine-kdevelopsessions.desktop
%{_datadir}/mime/packages/kdevelop.xml
%{_desktopdir}/kdevelop.desktop
%{_desktopdir}/kde4/kdevelop.desktop
%{_desktopdir}/kde4/kdevelop_ps.desktop
%{_iconsdir}/*/*x*/*/*.png
%{_includedir}/kdevelop

%files devel
%defattr(644,root,root,755)
%{_datadir}/apps/cmake/modules/FindKDevelop.cmake
