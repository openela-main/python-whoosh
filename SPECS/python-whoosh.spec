%if 0%{?fedora} || 0%{?rhel} >= 7
%global with_python3 1
%endif

%global mod_name Whoosh

%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-whoosh
Version:        2.7.4
Release:        9%{?dist}
Summary:        Fast, pure-Python full text indexing, search, and spell checking library 

License:        BSD 
URL:            http://pythonhosted.org/Whoosh/
Source0:        https://pypi.python.org/packages/source/W/%{mod_name}/%{mod_name}-%{version}.tar.gz

BuildArch:      noarch

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest
%endif # with python2

%if 0%{?with_python3}
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-pytest
BuildRequires: python%{python3_pkgversion}-sphinx
%endif

%description
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add search
functionality to their applications and websites. Every part of how Whoosh
works can be extended or replaced to meet your needs exactly.

%if %{with python2}
%package -n python2-whoosh
Summary:    Fast, Python3 full text indexing, search, and spell checking library
%{?python_provide:%python_provide python2-whoosh}

%description -n python2-whoosh
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add search
functionality to their applications and websites. Every part of how Whoosh
works can be extended or replaced to meet your needs exactly.
%endif # with python2

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-whoosh
Summary:    Fast, Python3 full text indexing, search, and spell checking library
%{?python_provide:%python_provide python%{python3_pkgversion}-whoosh}

%description -n python%{python3_pkgversion}-whoosh
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add search
functionality to their applications and websites. Every part of how Whoosh
works can be extended or replaced to meet your needs exactly.
%endif

%prep
%setup -q -n %{mod_name}-%{version}

%build
%if %{with python2}
%py2_build
%endif # with python2

%if 0%{?with_python3}
%py3_build
sphinx-build-3 docs/source docs/html
rm -f docs/html/.buildinfo
rm -rf docs/html/.doctrees
%endif

%install
%if %{with python2}
%py2_install
%endif # with python2

%if 0%{?with_python3}
%py3_install
%endif

%check
%if %{with python2}
%{__python2} setup.py test
%endif # with python2

%if 0%{?with_python3}
%{__python3} setup.py test
%endif

%if %{with python2}
%files -n python2-whoosh
%license LICENSE.txt
%doc docs/html/ README.txt
%{python2_sitelib}/*.egg-info/
%{python2_sitelib}/whoosh
%endif # with python2

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-whoosh
%license LICENSE.txt
%doc README.txt docs/html/
%{python3_sitelib}/whoosh
%{python3_sitelib}/*.egg-info/
%endif

%changelog
* Thu Jun 14 2018 Charalampos Stratakis <cstratak@redhat.com> - 2.7.4-9
- Conditionalize the python2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.7.4-5
- Enable tests

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.7.4-4
- Rebuild for Python 3.6
- Disable python3 tests for now

* Wed Oct 12 2016 Orion Poplawski <orion@cora.nwra.com> - 2.7.4-3
- Ship python2-whoosh
- Build python3 package for EPEL7
- Modernize spec

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.4-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun May 01 2016 Robert Kuska <rkuska@gmail.com> - 2.7.4-1
- Update to version 2.7.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Robert Kuska <rkuska@redhat.com> 2.7.0-1
- Update to version 2.7.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 30 2014 Robert Kuska <rkuska@redhat.com> - 2.7.5-4
- Change spec for el6 and epel7

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Robert Kuska <rkuska@redhat.com> - 2.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar 03 2014 Robert Kuska <rkuska@redhat.com> - 2.5.7-1
- Rebase to 2.5.7

* Mon Jan 27 2014 Robert Kuska <rkuska@redhat.com> - 2.5.6-1
- Rebase to 2.5.6

* Tue Nov 19 2013 Robert Kuska <rkuska@redhat.com> - 2.5.5-1
- Rebase to 2.5.5

* Mon Sep 09 2013 Robert Kuska <rkuska@redhat.com> - 2.5.3-1
- Rebase to 2.5.3

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Robert Kuska <rkuska@redhat.com> - 2.5.1-1
- Update source
- Add python3 subpackage (rhbz#979235)

* Mon Apr 08 2013 Robert Kuska <rkuska@redhat.com> - 2.4.1-2
- Review fixes

* Fri Apr 05 2013 Robert Kuska <rkuska@redhat.com> - 2.4.1-1
- Initial package

